from neomodel import (
    StructuredNode, StructuredRel, StringProperty, IntegerProperty, FloatProperty,
    RelationshipTo, RelationshipFrom, config
)
from faker import Faker
import random

from noSQL.models.edge.filipEdges import CultivatesRel, WorshipsRel
from noSQL.models.nodes.filipNodes import generate_cultures, generate_religions, generate_social_groups, generate_pops, \
    generate_localisations

config.DATABASE_URL = 'bolt://test:Filip1234@localhost:7687'

def generate_data(n):
    fake = Faker()
    cultures = []
    religions = []
    socialGroups = []
    localisations = []
    populations = []

    # Generowanie węzłów
    cultures.extend(generate_cultures(n, fake))
    religions.extend(generate_religions(n, fake))
    socialGroups.extend(generate_social_groups(n, fake))
    populations.extend(generate_pops(n))
    localisations.extend(generate_localisations(n, fake))

    for pop in populations:
        culture = random.choice(cultures)
        pop.cultivates.connect(culture,{"sentiment_level": random.randint(1, 10)})

        # Dodanie relacji RESIDES
        localisation = random.choice(localisations)
        pop.resides.connect(localisation)

        # Dodanie relacji WORSHIPS
        religion = random.choice(religions)
        pop.worship.connect(religion, {"religious_level":random.randint(1, 10)})

        # Dodanie relacji ISPARTOF
        socialGroup = random.choice(socialGroups)
        pop.isPartOf.connect(socialGroup)

    for culture in cultures:
        culture.save()
    for religion in religions:
        religion.save()
    for socialGroup in socialGroups:
        socialGroup.save()
    for localisation in localisations:
        localisation.save()
    for population in populations:
        population.save()

if __name__ == "__main__":
    generate_data(5)