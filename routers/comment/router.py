from fastapi import APIRouter

from schemes.comment.schema import CommentCreateSchema, CommentUpdateSchema
from services.comment.CommentService import CommentService

router = APIRouter(prefix="/comment")


@router.post("/create")
async def create_comment(comment: CommentCreateSchema):
    CommentService.create(comment.author_id, comment.product_id, comment.comment)
    return {"status": "created"}


@router.get("/all")
async def read_all_comments():
    comments = CommentService.read_all()
    return {"comments": comments}


@router.get("/{comment_id}")
async def read_comment_by_id(comment_id: int):
    comment = CommentService.read_by_id(comment_id)
    return {"comment": comment}


@router.post("/update")
async def update_comment_by_id(comment: CommentUpdateSchema):
    CommentService.update_by_id(comment.id, comment.new_author_id, comment.new_product_id, comment.new_comment)
    return {"status": "updated"}


@router.delete("/delete/{comment_id}")
async def delete_comment(comment_id: int):
    CommentService.delete_by_id(comment_id)
    return {"status": "deleted"}
