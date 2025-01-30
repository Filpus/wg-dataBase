from neomodel import (
    StructuredNode, StructuredRel, StringProperty, IntegerProperty, FloatProperty,
    RelationshipTo, RelationshipFrom, config
)
from faker import Faker
import random

from models.edges import *
from models.nodes import *

config.DATABASE_URL = 'bolt://ala:Vanitas1234!@localhost:7687'

def generate_data(n):
    fake = Faker()
    cultures = []
    religions = []
    socialGroups = []
    localisations = []
    populations = []
    events=[]
    resources=[]
    users=[]
    nations=[]
    actions=[]
    unit_types = []
    armies = []
    trade_agreements = []

    # Generowanie węzłów
    cultures.extend(generate_cultures(n, fake))
    religions.extend(generate_religions(n, fake))
    socialGroups.extend(generate_social_groups(n, fake))
    populations.extend(generate_pops(n))
    localisations.extend(generate_localisations(n, fake))
    events.extend(generate_events(n, fake))
    users.extend(generate_users(n, fake))
    resources.extend(generate_resources(n, fake))
    nations.extend(generate_nations(n, fake))
    actions.extend(generate_actions(n, fake))
    unit_types.extend(generate_unit_types(n, fake))
    armies.extend(generate_armies(n, fake))
    trade_agreements.extend((generate_trade_agreements(n,fake)))


    for event in events:
        n=random.randint(0,4)
        for i in range(n):
            type=random.randint(1,4)
            isNum=bool(random.randint(0,1))
            match type:
                case 1:
                    group=random.choice(socialGroups)
                    if(isNum):
                        event.groupNumModifies.connect(group,{"value": random.randint(1, 100)})
                    else:
                        event.groupPercModifies.connect(group,{"value": random.randint(1, 100)})
                case 2:
                    culture=random.choice(cultures)
                    if(isNum):
                        event.cultureNumModifies.connect(culture,{"value": random.randint(1, 100)})
                    else:
                        event.culturePercModifies.connect(culture,{"value": random.randint(1, 100)})
                case 3:
                    religion=random.choice(religions)
                    if(isNum):
                        event.religionNumModifies.connect(religion,{"value": random.randint(1, 100)})
                    else:
                        event.religionPercModifies.connect(religion,{"value": random.randint(1, 100)})
                case 4:
                    resource=random.choice(resources)
                    if(isNum):
                        event.resourceNumModifies.connect(resource,{"value": random.randint(1, 100)})
                    else:
                        event.resourcePercModifies.connect(resource,{"value": random.randint(1, 100)})


    for nation in nations:
        evs=random.choices(events)
        for e in evs:
            nation.takesPartInEvent.connect(e, {})

    for socialGroup in socialGroups:

        resource = random.choice(resources)
        socialGroup.consume.connect(resource,{"count": random.randint(1, 5)})
        resource = random.choice(resources)
        socialGroup.produce.connect(resource,{"effectiveness": random.randint(1, 10)})
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

    for nation in nations:
        religion = random.choice(religions)
        nation.worshipsNationally.connect(religion)

        culture = random.choice(cultures)
        nation.cultivatesNationally.connect(culture)

        resource = random.choice(resources)
        nation.owning.connect(resource, {"amount": random.randint(10, 100)})

        num_actions = random.randint(1, 3)
        for _ in range(num_actions):
            action = random.choice(actions)
            action.performedBy.connect(nation)

    for user in users:
        num_access = random.randint(1, 3)
        for _ in range(num_access):
            nation = random.choice(nations)
            user.nationAccess.connect(
                nation,
                {
                    "permisionName": fake.word(),
                    "isActive": bool(random.randint(0, 1)),
                    "dateAcquired": fake.date_time_this_year()
                }
            )
    for localisation in localisations:
        nation = random.choice(nations)
        localisation.placeIn.connect(nation)

    for army in armies:
        nation = random.choice(nations)
        army.belongsTo.connect(nation)
        for i in range(random.randint(1, 15)):
            troop = random.choice(unit_types)
            army.availableTroops.connect(troop,{"quantity": troop.volunteersNeeded})

    for unit in unit_types:
        resource_cost=random.choices(resources)
        for res in resource_cost:
            unit.costToMaintain.connect(res, {"quantity": random.randint(0,10)})


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
    for user in users:
        user.save()
    for event in events:
        event.save()
    for resource in resources:
        resource.save()
    for nation in nations:
        nation.save()
    for action in actions:
        action.save()
    for unit_type in unit_types:
        unit_type.save()
    for army in armies:
        army.save()
    for trade_agreement in trade_agreements:
        trade_agreement.save()


if __name__ == "__main__":
    generate_data(20)