from collections import namedtuple
from faker import Faker
import random
from dataGeneration.config import *

modifiersCount=100

Modifier= namedtuple("Modifier",["id","event","target","resource","socialGroup", "culture","religion"])


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
        modifier=Modifier(i, random.randint(0,eventsCount-1),ennum[random.randint(0,1)],random.randint(0,resourceCount-1),random.randint(0,groupsCount-1),random.randint(0,cultureCount-1),random.randint(0,religionsCount-1))
        modifiers.append(modifier)

    return modifiers


