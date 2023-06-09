from fastapi import APIRouter

from schemes.offer.schema import OfferCreateSchema, OfferUpdateSchema
from services.offer.OfferService import OfferService

router = APIRouter(prefix="/offer")


@router.post("/create")
async def create_offer(offer: OfferCreateSchema):
    OfferService.create(
        offer.creator_id,
        offer.partner_id,
        offer.give_product_id,
        offer.take_product_id,
        offer.is_accepted,
    )
    return {"status": "created"}


@router.get("/all")
async def read_all_offers():
    offers = OfferService.read_all()
    return {"offers": offers}


@router.get("/{offer_id}")
async def read_offer_by_id(offer_id: int):
    offer = OfferService.read_by_id(offer_id)
    return {"offer": offer}


@router.post("/update")
async def update_offer_by_id(offer: OfferUpdateSchema):
    OfferService.update_by_id(
        offer.id,
        offer.new_creator_id,
        offer.new_partner_id,
        offer.new_give_product_id,
        offer.new_take_product_id,
        offer.new_is_accepted
    )
    return {"status": "updated"}


@router.delete("/delete/{offer_id}")
async def delete_offer(offer_id: int):
    OfferService.delete_by_id(offer_id)
    return {"status": "deleted"}
