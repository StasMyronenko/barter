from schemes.base.schema import BaseCreatingSchema, BaseSchema


class CommentCreateSchema(BaseCreatingSchema):
    author_id: int
    product_id: int
    comment: str


class CommentSchema(BaseSchema, CommentCreateSchema):
    pass


class CommentUpdateSchema(BaseSchema):
    new_author_id: int | None
    new_product_id: int | None
    new_comment: str | None
