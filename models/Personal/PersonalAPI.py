from typing import Type

from sqlalchemy import select, Sequence
from sqlalchemy.orm import Session

from models.Personal.PersonalModel import Personal


class PersonalAPI:
    @staticmethod
    def create(session: Session, name: str, salary: int):
        personal = Personal(name=name, salary=salary)
        session.add(personal)

    @staticmethod
    def read_all(session: Session) -> Sequence["Personal"]:
        statement = select(Personal)
        personal = session.scalars(statement).all()
        return personal

    @staticmethod
    def read_by_id(session: Session, id_: int) -> Type["Personal"] | None:
        personal = session.get(Personal, id_)
        return personal

    @staticmethod
    def update_by_id(session: Session, id_: int, new_name: str | None, new_salary: int | None):
        personal = session.get(Personal, id_)
        if new_name:
            personal.name = new_name
        if new_salary:
            personal.salary = new_salary

    @staticmethod
    def delete_by_id(session: Session, id_: int) -> None:
        personal = session.get(Personal, id_)
        session.delete(personal)
