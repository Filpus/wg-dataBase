from collections import namedtuple
from faker import Faker
import random
from dataGeneration.config import *



Troops= namedtuple("Troops",["id","quantity","army","unitType"])


def generateTroops():
    armiesCount = ARMIES_COUNT
    unitTypes = UNIT_TYPE_COUNT
    fake=Faker()
    rows=[]
    for i in range(TROOPS_COUNT):
        row=Troops(i, random.randint(MIN_TROOPS_QUANTITY,MAX_TROOPS_QUANTITY), random.randint(0,armiesCount-1), random.randint(0,unitTypes-1))
        rows.append(row)

    return rows


