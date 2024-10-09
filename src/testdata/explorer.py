from src.model.explorer import Explorer

from typing import List, Optional


_explorers = [
    Explorer(name="Claude",
             country="FR",
             description="Scarce during full moons"),
    Explorer(name="Noah Weiser",
             country="DE",
             description="Myopic machete man"),
]


def get_all() -> List[Explorer]:
    return _explorers


def get_by_name(name: str) -> Optional[Explorer]:
    for _explorer in _explorers:
        if _explorer.name == name:
            return _explorer


def create(explorer: Explorer) -> Explorer:
    _explorers.append(explorer)
    return explorer


def modify(id, explorer: Explorer) -> Explorer:
    raise NotImplementedError


def replace(id, explorer: Explorer) -> Explorer:
    raise NotImplementedError
