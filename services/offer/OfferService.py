from handlers.error_handlers.session_error_handler import handle_session_error
from models.Offer.OfferAPI import OfferAPI
from services.BaseService import BaseServiceClass


class OfferService(BaseServiceClass):
    @staticmethod
    def create(
            creator_id: int,
            partner_id: int,
            give_product_id: int,
            take_product_id: int,
            is_accepted: bool,
    ):
        handle_session_error(
            OfferAPI.create,
            creator_id=creator_id,
            partner_id=partner_id,
            give_product_id=give_product_id,
            take_product_id=take_product_id,
            is_accepted=is_accepted,
        )

    @staticmethod
    def read_all():
        return handle_session_error(OfferAPI.read_all, do_commit=False)

    @staticmethod
    def read_by_id(id_: int):
        return handle_session_error(OfferAPI.read_by_id, do_commit=False, id_=id_)

    @staticmethod
    def update_by_id(
            id_: int,
            new_creator_id: int | None,
            new_partner_id: int | None,
            new_give_product_id: int | None,
            new_take_product_id: int | None,
            new_is_accepted: bool | None,
    ):
        handle_session_error(
            OfferAPI.update_by_id,
            id_=id_,
            new_creator_id=new_creator_id,
            new_partner_id=new_partner_id,
            new_give_product_id=new_give_product_id,
            new_take_product_id=new_take_product_id,
            new_is_accepted=new_is_accepted,
        )

    @staticmethod
    def delete_by_id(id_: int):
        handle_session_error(OfferAPI.delete_by_id, id_=id_)
