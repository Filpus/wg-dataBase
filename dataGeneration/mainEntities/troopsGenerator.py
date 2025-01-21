from collections import namedtuple
from faker import Faker
import random
from dataGeneration.config import *



Troops= namedtuple("Troops",["quantity","army","unitType"])


def generateTroops():
    armiesCount = ARMIES_COUNT
    unitTypes = UNIT_TYPE_COUNT
    fake=Faker()
    rows=[]
    for i in range(TROOPS_COUNT):
        row=Troops(random.randint(MIN_TROOPS_QUANTITY,MAX_TROOPS_QUANTITY), random.randint(1,armiesCount), random.randint(1,unitTypes))
        rows.append(row)

    return rows


