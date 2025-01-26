from neomodel import StructuredNode, StringProperty, BooleanProperty, RelationshipTo
import random

from noSQL.models.edge import (
    PerformedByRel,
    OwnedByRel,
    WorshipsNationallyRel,
    CultivatesNationallyRel,
    OrdersRel,
    HaveAccessToRel,
    OwningRel
)

class Action(StructuredNode):
    name = StringProperty(required=True, unique_index=True)
    isSettled = BooleanProperty(required=True)
    description = StringProperty(required=False)

    performedBy = RelationshipTo("Nation", "PERFORMEDBY", model=PerformedByRel)


class Nation(StructuredNode):
    name = StringProperty(required=True, unique_index=True)

    worshipsNationally = RelationshipTo("Religion", "WORSHIPSNATIONALLY", model=WorshipsNationallyRel)
    cultivatesNationally = RelationshipTo("Culture", "CULTIVATESNATIONALLY", model=CultivatesNationallyRel)
    orders = RelationshipTo("UnitType", "ORDERS", model=OrdersRel)
    haveAccessTo = RelationshipTo("UnitType", "HAVEACCESSTO", model=HaveAccessToRel)
    owning = RelationshipTo("Resource", "OWNING", model=OwningRel)

def generate_actions(n, fake):
    """
    Creates and saves 'n' Action nodes with random/fake data.
    """
    actions = []
    for _ in range(n):
        action = Action(
            name=fake.sentence(nb_words=3),
            isSettled=bool(random.getrandbits(1)),
            description=fake.text()
        ).save()
        actions.append(action)
    return actions

def generate_nations(n, fake):
    """
    Creates and saves 'n' Nation nodes with random/fake data.
    """
    nations = []
    for _ in range(n):
        nation = Nation(
            name=fake.country()
        ).save()
        nations.append(nation)
    return nations