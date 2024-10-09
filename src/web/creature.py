import src.testdata.creature as service

from fastapi import APIRouter
from typing import List, Optional
from src.model.creature import Creature


router = APIRouter(prefix="/creature")


@router.get("/")
def get_all() -> List[Creature]:
    return service.get_all()


@router.get("/{name}")
def get_by_name(name: str) -> Optional[Creature]:
    return service.get_by_name(name)


@router.post("/")
def create(creature: Creature) -> Creature:
    return service.create(creature)


@router.patch("/")
def modify(creature: Creature) -> Creature:
    return service.modify(creature)


@router.put("/")
def replace(creature: Creature) -> Creature:
    return service.replace(creature)


@router.delete("/{name}")
def delete(name: str):
    pass
