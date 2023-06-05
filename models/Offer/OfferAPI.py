from typing import Type

from sqlalchemy import select, Sequence
from sqlalchemy.orm import Session

from models.Offer.OfferModel import Offer


class OfferAPI:
    @staticmethod
    def create(
            session: Session,
            creator_id: int,
            partner_id: int,
            give_product_id: int,
            take_product_id: int,
            is_accepted: bool,
               ):
        offer = Offer(
            creator_id=creator_id,
            partner_id=partner_id,
            give_product_id=give_product_id,
            take_product_id=take_product_id,
            is_accepted=is_accepted
        )
        session.add(offer)

    @staticmethod
    def read_all(session: Session) -> Sequence["Offer"]:
        statement = select(Offer)
        offers = session.scalars(statement).all()
        return offers

    @staticmethod
    def read_by_id(session: Session, id_: int) -> Type["Offer"] | None:
        offer = session.get(Offer, id_)
        return offer

    @staticmethod
    def update_by_id(
            session: Session,
            id_: int,
            new_creator_id: int | None,
            new_partner_id: int | None,
            new_give_product_id: int | None,
            new_take_product_id: int | None,
            new_is_accepted: bool | None,
    ):
        offer = session.get(Offer, id_)
        if new_creator_id:
            offer.creator_id = new_creator_id
        if new_partner_id:
            offer.partner_id = new_partner_id
        if new_give_product_id:
            offer.give_product_id = new_give_product_id
        if new_take_product_id:
            offer.take_product_id = new_take_product_id
        if new_is_accepted:
            offer.is_accepted = new_is_accepted

    @staticmethod
    def delete_by_id(session: Session, id_: int) -> None:
        offer = session.get(Offer, id_)
        session.delete(offer)
