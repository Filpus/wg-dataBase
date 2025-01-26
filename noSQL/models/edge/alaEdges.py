from neomodel import StructuredNode, StructuredRel, StringProperty, FloatProperty, IntegerProperty, Relationship, \
    RelationshipTo, BooleanProperty, DateTimeProperty


class PercentModifierRel(StructuredRel):
    value = IntegerProperty(required= True)

class NumericalModifierRel(StructuredRel):
    value = IntegerProperty(required=True)

class AccessToNationRel(StructuredRel):
    permisionName = StringProperty(required=True)
    isActive = BooleanProperty(required=True)
    dateAcquired= DateTimeProperty(required=True)
