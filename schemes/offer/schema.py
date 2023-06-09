from schemes.base.schema import BaseCreatingSchema, BaseSchema


class OfferCreateSchema(BaseCreatingSchema):
    creator_id: int
    partner_id: int
    give_product_id: int
    take_product_id: int
    is_accepted: bool


class OfferSchema(BaseSchema, OfferCreateSchema):
    pass


class OfferUpdateSchema(BaseSchema):
    new_creator_id: int | None
    new_partner_id: int | None
    new_give_product_id: int | None
    new_take_product_id: int | None
    new_is_accepted: bool | None
