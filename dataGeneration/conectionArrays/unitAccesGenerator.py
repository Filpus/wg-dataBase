from collections import namedtuple
from faker import Faker
import random


accessCount=100
UnitAccess= namedtuple("UnitAccess",["id","nation","unitType"])


def generateUnitAccess(nationCount,unitTypeCount):
    fake=Faker()
    rows=[]
    for i in range(accessCount):
        row=UnitAccess(i, random.randint(0,nationCount), random.randint(0,unitTypeCount))
        if row not in rows:
            rows.append(row)


    return rows


print(generateUnitAccess(200,50))