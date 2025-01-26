from neomodel import (
    StructuredNode, StructuredRel, StringProperty, IntegerProperty, FloatProperty,
    RelationshipTo, RelationshipFrom, config
)
from faker import Faker
import random

from noSQL.models.nodes.filipNodes import generate_cultures, generate_religions, generate_social_groups, generate_pops, \
    generate_localisations

config.DATABASE_URL = 'bolt://test:Filip1234@localhost:7687'

def generate_data(n):
    fake = Faker()
    cultures = []
    religions = []
    socialGroups = []
    localisations = []
    pop = []

    # Generowanie węzłów
    cultures.extend(generate_cultures(n, fake))
    religions.extend(generate_religions(n, fake))
    socialGroups.extend(generate_social_groups(n, fake))
    pop.extend(generate_pops(n))
    localisations.extend(generate_localisations(n, fake))


if __name__ == "__main__":
    generate_data(5)