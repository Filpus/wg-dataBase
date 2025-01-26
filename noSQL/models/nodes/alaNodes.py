import random

from neo4j.graph import Relationship
from neo4j.time import Duration
from neomodel import StructuredNode, StringProperty, FloatProperty, IntegerProperty, RelationshipTo, BooleanProperty

from noSQL.models.edge.alaEdges import NumericalModifierRel, PercentModifierRel, AccessToNationRel
from noSQL.models.edge.wojtekEdges import *
from noSQL.models.nodes.filipNodes import *

class Resource(StructuredNode):
    name = StringProperty(required=True, unique_index=True)
    isMain = BooleanProperty(required=True)

class User(StructuredNode):
    name=StringProperty(required=True)
    email=StringProperty(required=True)
    password=StringProperty(required=True)
    isArchived= BooleanProperty(required=True)

    nationAccess = RelationshipTo("Nation", "HASACCESTO", model= AccessToNationRel)

class Event(StructuredNode):
    name=StringProperty(required=True)
    description=StringProperty(required=True)
    duration=IntegerProperty(required=False)
    cultureNumModifies = RelationshipTo("Culture", "MODIFIESBYNUM", model= NumericalModifierRel)
    culturePercModifies = RelationshipTo("Culture", "MODIFIESBYPERC", model= PercentModifierRel)

    religionNumModifies = RelationshipTo("Religion", "MODIFIESBYNUM", model= NumericalModifierRel)
    religionPercModifies = RelationshipTo("Religion", "MODIFIESBYPERC", model= PercentModifierRel)

    groupNumModifies = RelationshipTo("SocialGroup", "MODIFIESBYNUM", model= NumericalModifierRel)
    groupPercModifies = RelationshipTo("SocialGroup", "MODIFIESBYPERC", model= PercentModifierRel)

    resourceNumModifies = RelationshipTo("Resource", "MODIFIESBYNUM", model= NumericalModifierRel)
    resourcePercModifies = RelationshipTo("Resource", "MODIFIESBYPERC", model= PercentModifierRel)

    happensIn = RelationshipTo("Nation", "HAPPENSIN", model= HappensInRel)



def generate_resources(n,fake):
    resources = []
    for _ in range(n):
        resource = Resource(
            name=fake.unique.word(),
            isMain=bool(random.getrandbits(1))
        ).save()
        resources.append(resource)
    return resources

def generate_users(n,fake):
    users = []
    for _ in range(n):
        user = User(
            name=fake.name(),
            email=fake.unique.email(),
            password=fake.password(),
            isArchived=bool(random.getrandbits(1))
        ).save()
        users.append(user)
    return users

def generate_events(n,fake):
    events = []
    for _ in range(n):
        event = Event(
            name=fake.sentence(nb_words=3),
            description=fake.text(),
            duration=random.randint(1, 10)
        ).save()
        events.append(event)
    return events
