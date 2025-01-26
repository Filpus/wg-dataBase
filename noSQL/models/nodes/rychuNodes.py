import random
from models.edge.rychuEdges import *
from neomodel import StructuredNode, StringProperty, IntegerProperty, RelationshipTo, BooleanProperty
from noSQL.models.edge import AvailableTroopsRel, CostToMaintainRel, CostToProduceRel, WantsResourcesRel, \
    OffersResourcesRel, BelongsToRel, StayingAtRel, IsOfferingRel


class TradeAgreement(StructuredNode):
    name = StringProperty(required=True, unique_index=True)
    isAccepted = BooleanProperty(required=True)
    wantsResources = RelationshipTo(cls_name="Resources", relation_type="WANTSRESOURCES", model=WantsResourcesRel)
    offersResources = RelationshipTo(cls_name="Resources", relation_type="OFFERSRESOURCES", model=OffersResourcesRel)
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
    costToMaintain = RelationshipTo(cls_name="Resources", relation_type="COSTTOMAINTAIN", model=CostToMaintainRel)
    costToProduce = RelationshipTo(cls_name="Resources", relation_type="COSTTOPRODUCE", model=CostToProduceRel)

class Army(StructuredNode):
    name = StringProperty(required=True, unique_index=True)
    availableTroops = RelationshipTo(cls_name="UnitType", relation_type="AVAILABLETROOPS", model=AvailableTroopsRel)
    belongsTo = RelationshipTo(cls_name="Nation", relation_type="BELONGSTO", model=BelongsToRel)
    stayingAt = RelationshipTo(cls_name="Army", relation_type="STAYINGAT", model=StayingAtRel)


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