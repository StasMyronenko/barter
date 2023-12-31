from sqlalchemy import Integer, ForeignKey, Boolean
from sqlalchemy.orm import Mapped, mapped_column, relationship

from models.Base import Base
from models.Product.ProductModel import Product
from models.User.UserModel import User


class Offer(Base):
    __tablename__ = 'offer'

    id: Mapped[int] = mapped_column(Integer, primary_key=True)

    creator_id: Mapped[int] = mapped_column(ForeignKey(f'{User.__tablename__}.{User.id.key}'))
    creator: Mapped[User] = relationship(User, foreign_keys=[creator_id])

    partner_id: Mapped[int] = mapped_column(ForeignKey(f'{User.__tablename__}.{User.id.key}'))
    partner: Mapped[User] = relationship(User, foreign_keys=[partner_id])

    give_product_id: Mapped[int] = mapped_column(ForeignKey(f'{Product.__tablename__}.{Product.id.key}'))
    give_product: Mapped[Product] = relationship(foreign_keys=[give_product_id])

    take_product_id: Mapped[int] = mapped_column(ForeignKey(f'{Product.__tablename__}.{Product.id.key}'))
    take_product: Mapped[Product] = relationship(foreign_keys=[take_product_id])

    is_accepted = mapped_column(Boolean, default=False)
