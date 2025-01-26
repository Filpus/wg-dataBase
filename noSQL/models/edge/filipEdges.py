from neomodel import StructuredNode, StructuredRel, StringProperty, FloatProperty, IntegerProperty, Relationship, RelationshipTo


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

