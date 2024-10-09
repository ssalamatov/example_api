from random import sample

from src.model.creature import Creature
from src.service import creature as service


creature = Creature(name="yeti",
             country="CN",
             area="Himalayas",
             description="Hirsute Himalayan",
             aka="Abominable Snowman",
             )


def test_create():
    assert service.create(creature) == creature
    assert service.get_by_name(creature.name) == creature
