from neomodel import StructuredRel, IntegerProperty

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