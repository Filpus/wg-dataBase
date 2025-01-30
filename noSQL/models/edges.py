from neomodel import StructuredNode, StructuredRel, StringProperty, FloatProperty, IntegerProperty, Relationship, \
    RelationshipTo, BooleanProperty, DateTimeProperty

# Ala

class PercentModifierRel(StructuredRel):
    value = IntegerProperty(required= True)

class NumericalModifierRel(StructuredRel):
    value = IntegerProperty(required=True)

class AccessToNationRel(StructuredRel):
    permisionName = StringProperty(required=True)
    isActive = BooleanProperty(required=True)
    dateAcquired= DateTimeProperty(required=True)

# Filip

class CultivatesRel(StructuredRel):
    sentiment_level = IntegerProperty()

class WorshipsRel(StructuredRel):
    religious_level = IntegerProperty()

class IsPartOfRel(StructuredRel):
    pass

class ProducesRel(StructuredRel):
    effectiveness = FloatProperty(required=True)
    required_satisfaction = FloatProperty()

class ConsumesRel(StructuredRel):
    count = IntegerProperty(required=True)
    satisfaction_debuff = FloatProperty()

class ResidesRel(StructuredRel):
    pass

# Rychu

class AvailableTroopsRel(StructuredRel):
    quantity = IntegerProperty(required=True)

class CostToMaintainRel(StructuredRel):
    quantity = IntegerProperty(required=True)

class CostToProduceRel(StructuredRel):
    quantity = IntegerProperty(required=True)

class WantsResourcesRel(StructuredRel):
    quantity = IntegerProperty(required=True)

class OffersResourcesRel(StructuredRel):
    quantity = IntegerProperty(required=True)

class LeadsRel(StructuredRel):
    pass

class StayingAtRel(StructuredRel):
    pass

class IsOfferingRel(StructuredRel):
    pass

class IsReceivingRel(StructuredRel):
    pass

# Wojtek

class PerformedByRel(StructuredRel):
    pass

class OwnedByRel(StructuredRel):
    pass

class WorshipsNationallyRel(StructuredRel):
    pass

class CultivatesNationallyRel(StructuredRel):
    pass

class OrdersRel(StructuredRel):
    quantity = IntegerProperty(required=True)

class HaveAccessToRel(StructuredRel):
    pass

class HappensInRel(StructuredRel):
    pass

class OwningRel(StructuredRel):
    amount = IntegerProperty(required=True)