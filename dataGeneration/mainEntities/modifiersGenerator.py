from collections import namedtuple
from faker import Faker
import random

modifiersCount=100

Modifier= namedtuple("Modifier",["id","event","target","resource","socialGroup", "culture","religion"])


def generateModifiers(eventsCount, resourceCount,groupsCount, cultureCount,religionsCount):
    fake=Faker()
    modifiers=[]
    for i in range(modifiersCount):
        modifier=Modifier(i, random.randint(0,eventsCount),random.randint(0,resourceCount),random.randint(0,groupsCount),random.randint(0,cultureCount),random.randint(0,religionsCount))
        modifiers.append(modifier)

    return modifiers


print(generateModifiers(100,10,8,50,70))