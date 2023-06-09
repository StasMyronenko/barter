from handlers.error_handlers.session_error_handler import handle_session_error
from models.User.UserAPI import UserAPI
from services.BaseService import BaseServiceClass


class UserService(BaseServiceClass):
    @staticmethod
    def create(name: str, number: str):
        handle_session_error(UserAPI.create, name=name, number=number)

    @staticmethod
    def read_all():
        return handle_session_error(UserAPI.read_all, do_commit=False)

    @staticmethod
    def read_by_id(id_: int):
        return handle_session_error(UserAPI.read_by_id, do_commit=False, id_=id_)

    @staticmethod
    def update_by_id(id_: int, new_name: str | None, new_number: str | None):
        handle_session_error(UserAPI.update_by_id, id_=id_, new_name=new_name, new_number=new_number)

    @staticmethod
    def delete_by_id(id_: int):
        handle_session_error(UserAPI.delete_by_id, id_=id_)
