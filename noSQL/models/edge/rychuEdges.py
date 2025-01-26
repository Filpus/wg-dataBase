from neomodel import StructuredRel, IntegerProperty

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

class BelongsToRel(StructuredRel):
    pass

class StayingAtRel(StructuredRel):
    pass

class IsOfferingRel(StructuredRel):
    pass

class IsReceivingRel(StructuredRel):
    pass