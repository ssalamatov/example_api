import src.testdata.explorer as service

from fastapi import APIRouter
from typing import List, Optional
from src.model.explorer import Explorer


router = APIRouter(prefix="/explorer")


@router.get("/")
def get_all() -> List[Explorer]:
    return service.get_all()


@router.get("/{name}")
def get_by_name(name: str) -> Optional[Explorer]:
    return service.get_by_name(name)


@router.post("/")
def create(explorer: Explorer) -> Explorer:
    return service.create(explorer)


@router.patch("/")
def modify(explorer: Explorer) -> Explorer:
    return service.modify(explorer)


@router.put("/")
def replace(explorer: Explorer) -> Explorer:
    return service.replace(explorer)


@router.delete("/{name}")
def delete(name: str):
    pass
