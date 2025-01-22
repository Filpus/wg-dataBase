from neo4j.graph import Relationship
from neomodel import StructuredNode, StringProperty, FloatProperty, IntegerProperty, RelationshipTo




class Culture(StructuredNode):
    name = StringProperty(required=True, unique_index=True)

class Religion(StructuredNode):
    name = StringProperty(required=True, unique_index=True)

class SocialGroup(StructuredNode):
    name = StringProperty(required=True, unique_index=True)
    base_satisfaction = FloatProperty(required=True,  default=0.5)
    volunteers = IntegerProperty()

class Pop(StructuredNode):
    satisfaction = FloatProperty(required=True, default=0.5)
class Localisation(StructuredNode):
    name = StringProperty(required=True)
    size = IntegerProperty(required=True)
    fortifications_level = IntegerProperty()
