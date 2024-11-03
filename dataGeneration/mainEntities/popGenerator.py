from collections import namedtuple
from faker import Faker
import random

from jupyterlab.semver import satisfies

from dataGeneration.config import *



Pop= namedtuple("Pop",["id","group","culture","religion","location", "satisfaction"])


def generatePops():
    fake=Faker()
    pops=[]
    for i in range(POP_COUNT):
        pop=Pop(i, random.randint(0,GROUP_COUNT-1), random.randint(0,CULTURE_COUNT-1),random.randint(0,RELIGION_COUNT-1),random.randint(0,LOCATION_COUNT-1),float(random.randint(0,100)/100))
        pops.append(pop)

    return pops


