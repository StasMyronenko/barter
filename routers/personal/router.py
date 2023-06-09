from fastapi import APIRouter

from schemes.personal.schema import PersonalCreateSchema, PersonalUpdateSchema
from services.personal.PersonalService import PersonalService

router = APIRouter(prefix="/personal")


@router.post("/create")
async def create_personal(personal: PersonalCreateSchema):
    PersonalService.create(personal.name, personal.salary)
    return {"status": "created"}


@router.get("/all")
async def read_all_personals():
    personals = PersonalService.read_all()
    return {"personals": personals}


@router.get("/{personal_id}")
async def read_personal_by_id(personal_id: int):
    personal = PersonalService.read_by_id(personal_id)
    return {"personal": personal}


@router.post("/update")
async def update_personal_by_id(personal: PersonalUpdateSchema):
    PersonalService.update_by_id(personal.id, personal.new_name, personal.new_salary)
    return {"status": "updated"}


@router.delete("/delete/{personal_id}")
async def delete_personal(personal_id: int):
    PersonalService.delete_by_id(personal_id)
    return {"status": "deleted"}
