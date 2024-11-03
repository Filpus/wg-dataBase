from collections import namedtuple
from faker import Faker
import random
from dataGeneration.config import *


Army= namedtuple("Army",  ["id","name", "nation","location"])


def generateArmies():
    nationNum = NATIONS_COUNT
    locationNum = LOCATION_COUNT
    fake=Faker()
    armies=[]
    for i in range(ARMIES_COUNT):
        army=Army(i,fake.word(),random.randint(0,nationNum-1),random.randint(0,locationNum-1))
        armies.append(army)

    return armies


