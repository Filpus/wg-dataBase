import random

from neo4j.graph import Relationship
from neomodel import StructuredNode, StringProperty, FloatProperty, IntegerProperty, RelationshipTo

from noSQL.models.edge.filipEdges import *


class Resource(StructuredNode):
    name = StringProperty(required=True, unique_index=True)
class Culture(StructuredNode):
    name = StringProperty(required=True, unique_index=True)

class Religion(StructuredNode):
    name = StringProperty(required=True, unique_index=True)

class SocialGroup(StructuredNode):
    name = StringProperty(required=True, unique_index=True)
    base_satisfaction = FloatProperty(required=True)
    volunteers = IntegerProperty()

class Pop(StructuredNode):
    satisfaction = FloatProperty(required=True)
    cultivates = RelationshipTo("Culure", "CULTIVATES", model= CultivatesRel)
    resides = RelationshipTo('Localisation', 'RESIDES', model= ResidesRel)
    worship = RelationshipTo("Religion", "WORSHIP", model=WorshipsRel)
    isPartOf = RelationshipTo("SocialGroup", "ISPARTOF", model=IsPartOfRel)

class Localisation(StructuredNode):
    name = StringProperty(required=True)
    size = IntegerProperty(required=True)
    fortifications_level = IntegerProperty()



def generate_cultures(n, fake):
    nodes = []
    for _ in range(n):
        nodes.append(Culture(name=fake.word()).save())
    return nodes

def generate_religions(n, fake):
    nodes = []
    for _ in range(n):
        nodes.append(Religion(name=fake.word()).save())
    return nodes

def generate_social_groups(n, fake):
    nodes = []
    for _ in range(n):
        nodes.append(SocialGroup(
            name=fake.word(),
            base_satisfaction=random.uniform(0.3, 0.9),
            volunteers=random.randint(10, 500)
        ).save())
    return nodes

def generate_pops(n):
    nodes = []
    for _ in range(n):
        nodes.append(Pop(satisfaction=round(random.uniform(0.2, 1.0),2)).save())
    return nodes

def generate_localisations(n, fake):
    nodes = []
    for _ in range(n):
        nodes.append(Localisation(
            name=fake.city(),
            size=random.randint(100, 1000),
            fortifications_level=random.randint(0, 10)
        ).save())
    return nodes