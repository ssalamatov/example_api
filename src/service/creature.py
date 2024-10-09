from src.model.creature import Creature

import src.testdata.creature as data


def get_all() -> list[Creature]:
    return data.get_all()


def get_by_name(name: str) -> Creature | None:
    return data.get_by_name(name)


def create(creature: Creature) -> Creature:
    return data.create(creature)


def replace(id, creature: Creature) -> Creature:
    return data.replace(id, creature)


def modify(id, creature: Creature) -> Creature:
    return data.modify(id, creature)
