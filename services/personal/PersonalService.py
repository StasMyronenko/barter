from handlers.error_handlers.session_error_handler import handle_session_error
from models.Personal.PersonalAPI import PersonalAPI
from services.BaseService import BaseServiceClass


class PersonalService(BaseServiceClass):
    @staticmethod
    def create(name: str, salary: int):
        handle_session_error(
            PersonalAPI.create,
            name=name,
            salary=salary,
        )

    @staticmethod
    def read_all():
        return handle_session_error(PersonalAPI.read_all, do_commit=False)

    @staticmethod
    def read_by_id(id_: int):
        return handle_session_error(PersonalAPI.read_by_id, do_commit=False, id_=id_)

    @staticmethod
    def update_by_id(
            id_: int,
            new_name: str | None,
            new_salary: int | None,
    ):
        handle_session_error(
            PersonalAPI.update_by_id,
            id_=id_,
            new_name=new_name,
            new_salary=new_salary,
        )

    @staticmethod
    def delete_by_id(id_: int):
        handle_session_error(PersonalAPI.delete_by_id, id_=id_)
