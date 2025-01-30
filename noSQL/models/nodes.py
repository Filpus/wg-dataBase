import random

from neo4j.graph import Relationship
from neo4j.time import Duration
from neomodel import StructuredNode, StringProperty, FloatProperty, IntegerProperty, RelationshipTo, BooleanProperty

from .edges import *

# Ala

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

# Filip

class Culture(StructuredNode):
    name = StringProperty(required=True, unique_index=True)

class Religion(StructuredNode):
    name = StringProperty(required=True, unique_index=True)

class SocialGroup(StructuredNode):
    name = StringProperty(required=True, unique_index=True)
    base_satisfaction = FloatProperty(required=True)
    volunteers = IntegerProperty()
    produce = RelationshipTo("Resource","PRODUCE", model=ProducesRel)
    consume = RelationshipTo("Resource","CONSUME", model=ConsumesRel)

class Pop(StructuredNode):
    satisfaction = FloatProperty(required=True)
    cultivates = RelationshipTo("Culture", "CULTIVATES", model= CultivatesRel)
    resides = RelationshipTo('Localisation', 'RESIDES', model= ResidesRel)
    worship = RelationshipTo("Religion", "WORSHIP", model=WorshipsRel)
    isPartOf = RelationshipTo("SocialGroup", "ISPARTOF", model=IsPartOfRel)

class Localisation(StructuredNode):
    name = StringProperty(required=True)
    size = IntegerProperty(required=True)
    fortifications_level = IntegerProperty()
    placeIn = RelationshipTo("Nation", "PLACEIN", model=placeIn)

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

# Rychu

class TradeAgreement(StructuredNode):
    name = StringProperty(required=True, unique_index=True)
    isAccepted = BooleanProperty(required=True)
    wantsResources = RelationshipTo(cls_name="Resource", relation_type="WANTSRESOURCES", model=WantsResourcesRel)
    offersResources = RelationshipTo(cls_name="Resource", relation_type="OFFERSRESOURCES", model=OffersResourcesRel)
    isOffering = RelationshipTo(cls_name="Nation", relation_type="ISOFFERING", model=IsOfferingRel)

    # It's better to start from Nation so we have (Nation--offers->TRADEAGREEMENT--receices->Nation)
    #isReceiving = RelationshipTo(cls_name="Nation", relation_type="ISRECEIVING", model=IsReceivingRel)
class UnitType(StructuredNode):
    name = StringProperty(required=True, unique_index=True)
    melee = IntegerProperty(required=True)
    range = IntegerProperty(required=True)
    speed = IntegerProperty(required=True)
    morale = IntegerProperty(required=True)
    volunteersNeeded = IntegerProperty(required=True)
    isNaval = BooleanProperty(required=True)
    costToMaintain = RelationshipTo(cls_name="Resource", relation_type="COSTTOMAINTAIN", model=CostToMaintainRel)
    costToProduce = RelationshipTo(cls_name="Resource", relation_type="COSTTOPRODUCE", model=CostToProduceRel)

class Army(StructuredNode):
    name = StringProperty(required=True, unique_index=True)
    availableTroops = RelationshipTo(cls_name="UnitType", relation_type="AVAILABLETROOPS", model=AvailableTroopsRel)
    stayingAt = RelationshipTo(cls_name="Localisation", relation_type="STAYINGAT", model=StayingAtRel)
    belongsTo = RelationshipTo(cls_name="Nation", relation_type="BELONGSTO", model=BelongsToRel)

def generate_armies(n, fake):
    armies = []
    for _ in range(n):
        army = Army(name=fake.unique.word()).save()
        armies.append(army)
    return armies

def generate_trade_agreements(n, fake):
    trade_agreements = []
    for _ in range(n):
        trade_agreement = TradeAgreement(
            name=fake.unique.word(),
            isAccepted = bool(random.getrandbits(1))
        ).save()
        trade_agreements.append(trade_agreement)
    return trade_agreements

def generate_unit_types(n, fake):
    units = []
    for _ in range(n):
        unit = UnitType(
            name=fake.unique.word(),
            melee=random.randint(1, 10),
            range=random.randint(1, 10),
            speed=random.randint(1, 10),
            morale=random.randint(1, 10),
            volunteersNeeded=random.randint(1, 10),
            isNaval = bool(random.getrandbits(1)),
        ).save()
        units.append(unit)
    return units

# Wojtek

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
    isReceiving = RelationshipTo(cls_name="TradeAgreement", relation_type="ISRECEIVING", model=IsReceivingRel)
    takesPartInEvent = RelationshipTo(cls_name="Event", relation_type="TAKESPART", model=TakesPartRel)

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