from collections import namedtuple
from faker import Faker
import random

from jupyterlab.semver import satisfies

from dataGeneration.config import *



Pop= namedtuple("Pop",["group","culture","religion","location", "satisfaction"])


def generatePops():
    fake=Faker()
    pops=[]
    for i in range(POP_COUNT):
        pop=Pop( random.randint(1,GROUP_COUNT), random.randint(1,CULTURE_COUNT),random.randint(1,RELIGION_COUNT),random.randint(1,LOCATION_COUNT),float(random.randint(0,100)/100))
        pops.append(pop)

    return pops


