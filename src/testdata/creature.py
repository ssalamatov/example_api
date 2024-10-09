from src.model.creature import Creature

from typing import List, Optional

_creatures = [
    Creature(name="Yeti",
             aka="Abominable Snowman",
             country="CN",
             area="Himalayas",
             description="Hirsute Himalayan"),
    Creature(name="Bigfoot",
             description="Yeti's Cousin Eddie",
             country="US",
             area="*",
             aka="Sasquatch"),
]


def get_all() -> List[Creature]:
    return _creatures


def get_by_name(name: str) -> Optional[Creature]:
    for _creature in _creatures:
        if _creature.name == name:
            return _creature


def create(creature: Creature) -> Creature:
    _creatures.append(creature)
    return creature


def modify(id, creature: Creature) -> Creature:
    raise NotImplementedError


def replace(id, creature: Creature) -> Creature:
    raise NotImplementedError
