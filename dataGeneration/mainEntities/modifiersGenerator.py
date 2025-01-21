from collections import namedtuple
from faker import Faker
import random
from dataGeneration.config import *

modifiersCount=100

Modifier= namedtuple("Modifier",["event","target","resource","socialGroup", "culture","religion"])


def generateModifiers():
    eventsCount = EVENT_COUNT
    resourceCount = RESOURCE_COUNT
    groupsCount = GROUP_COUNT
    cultureCount= CULTURE_COUNT
    religionsCount = RELIGION_COUNT
    ennum = ["Happiness","Production"]
    fake=Faker()
    modifiers=[]
    for i in range(MODIFIERS_COUNT):
        modifier=Modifier( random.randint(1,eventsCount),ennum[random.randint(0,1)],random.randint(1,resourceCount),random.randint(1,groupsCount),random.randint(1,cultureCount),random.randint(1,religionsCount))
        modifiers.append(modifier)

    return modifiers


