from handlers.error_handlers.session_error_handler import handle_session_error
from models.Product.ProductAPI import ProductAPI
from services.BaseService import BaseServiceClass


class ProductService(BaseServiceClass):
    @staticmethod
    def create(owner_id: int, description: str, title: str, image_url: str):
        handle_session_error(
            ProductAPI.create,
            owner_id=owner_id,
            description=description,
            title=title,
            image_url=image_url
        )

    @staticmethod
    def read_all():
        return handle_session_error(ProductAPI.read_all, do_commit=False)

    @staticmethod
    def read_by_id(id_: int):
        return handle_session_error(ProductAPI.read_by_id, do_commit=False, id_=id_)

    @staticmethod
    def update_by_id(
            id_: int,
            new_owner_id: int | None,
            new_description: str | None,
            new_title: str | None,
            new_image_url: str | None
    ):
        handle_session_error(
            ProductAPI.update_by_id,
            id_=id_,
            new_owner_id=new_owner_id,
            new_description=new_description,
            new_title=new_title,
            new_image_url=new_image_url,
        )

    @staticmethod
    def delete_by_id(id_: int):
        handle_session_error(ProductAPI.delete_by_id, id_=id_)
