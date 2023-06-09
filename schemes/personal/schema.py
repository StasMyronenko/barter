from schemes.base.schema import BaseCreatingSchema, BaseSchema


class PersonalCreateSchema(BaseCreatingSchema):
    name: str
    salary: int


class PersonalSchema(BaseSchema, PersonalCreateSchema):
    pass


class PersonalUpdateSchema(BaseSchema):
    new_name: str | None
    new_salary: int | None
