from collections import namedtuple
from faker import Faker
import random
from dataGeneration.config import *



UnitAccess= namedtuple("UnitAccess",["nation","unitType"])
existingAccesses=set()

def generateUnitAccess():
    nationCount = NATIONS_COUNT
    unitTypeCount = UNIT_TYPE_COUNT
    fake=Faker()
    rows=[]
    for i in range(ACCESS_COUNT):
        row=UnitAccess( random.randint(1,nationCount), random.randint(1,unitTypeCount))
        access = (row.nation, row.unitType)
        if row not in rows and access not in existingAccesses:
            existingAccesses.add(access)
            rows.append(row)


    return rows


