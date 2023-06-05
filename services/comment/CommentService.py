from handlers.error_handlers.session_error_handler import handle_session_error
from models.Comment.CommentAPI import CommentAPI
from services.BaseService import BaseServiceClass


class CommentService(BaseServiceClass):
    @staticmethod
    def create(
            author_id: int,
            product_id: int,
            comment: str
    ):
        handle_session_error(
            CommentAPI.create,
            author_id=author_id,
            product_id=product_id,
            comment=comment,
        )

    @staticmethod
    def read_all():
        return handle_session_error(CommentAPI.read_all, do_commit=False)

    @staticmethod
    def read_by_id(id_: int):
        return handle_session_error(CommentAPI.read_by_id, do_commit=False, id_=id_)

    @staticmethod
    def update_by_id(
            id_: int,
            new_author_id: int | None,
            new_product_id: int | None,
            new_comment: str | None,
    ):
        handle_session_error(
            CommentAPI.update_by_id,
            id_=id_,
            new_author_id=new_author_id,
            new_product_id=new_product_id,
            new_comment=new_comment,
        )

    @staticmethod
    def delete_by_id(id_: int):
        handle_session_error(CommentAPI.delete_by_id, id_=id_)
