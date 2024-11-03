from collections import namedtuple
from faker import Faker
import random
from dataGeneration.config import *



UnitAccess= namedtuple("UnitAccess",["id","nation","unitType"])


def generateUnitAccess():
    nationCount = NATIONS_COUNT
    unitTypeCount = UNIT_TYPE_COUNT
    fake=Faker()
    rows=[]
    for i in range(ACCESS_COUNT):
        row=UnitAccess(i, random.randint(0,nationCount-1), random.randint(0,unitTypeCount-1))
        if row not in rows:
            rows.append(row)


    return rows


