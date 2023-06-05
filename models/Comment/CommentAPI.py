from typing import Type

from sqlalchemy import select, Sequence
from sqlalchemy.orm import Session

from models.Comment.CommentModel import Comment


class CommentAPI:
    @staticmethod
    def create(
            session: Session,
            author_id: int,
            product_id: int,
            comment: str
    ):
        comment = Comment(
            author_id=author_id,
            product_id=product_id,
            comment=comment
        )
        session.add(comment)

    @staticmethod
    def read_all(session: Session) -> Sequence["Comment"]:
        statement = select(Comment)
        comments = session.scalars(statement).all()
        return comments

    @staticmethod
    def read_by_id(session: Session, id_: int) -> Type["Comment"] | None:
        comment = session.get(Comment, id_)
        return comment

    @staticmethod
    def update_by_id(
            session: Session,
            id_: int,
            new_author_id: int | None,
            new_product_id: int | None,
            new_comment: str | None,
    ):
        comment = session.get(Comment, id_)
        if new_author_id:
            comment.author_id = new_author_id
        if new_product_id:
            comment.product_id = new_product_id
        if new_comment:
            comment.comment = new_comment

    @staticmethod
    def delete_by_id(session: Session, id_: int) -> None:
        comment = session.get(Comment, id_)
        session.delete(comment)
