from sqlalchemy import Integer, ForeignKey, String
from sqlalchemy.orm import Mapped, mapped_column, relationship

from models.Base import Base
from models.Product.ProductModel import Product
from models.User.UserModel import User


class Comment(Base):
    __tablename__ = 'comment'

    id: Mapped[int] = mapped_column(Integer, primary_key=True)

    author_id: Mapped[int] = mapped_column(ForeignKey(f'{User.__tablename__}.{User.id.key}'))
    author: Mapped[User] = relationship()

    product_id: Mapped[int] = mapped_column(ForeignKey(f'{Product.__tablename__}.{Product.id.key}'))
    product: Mapped[Product] = relationship()

    comment = mapped_column(String)
