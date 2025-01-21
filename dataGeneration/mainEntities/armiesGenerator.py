from collections import namedtuple
from faker import Faker
import random
from dataGeneration.config import *


Army= namedtuple("Army",  ["name", "nation","location"])


def generateArmies():
    nationNum = NATIONS_COUNT
    locationNum = LOCATION_COUNT
    fake=Faker()
    armies=[]
    for i in range(ARMIES_COUNT):
        army=Army(fake.word(),random.randint(1,nationNum),random.randint(1,locationNum))
        armies.append(army)

    return armies


