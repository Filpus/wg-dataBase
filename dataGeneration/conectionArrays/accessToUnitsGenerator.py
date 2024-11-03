from collections import namedtuple
from faker import Faker
import random

accessCount=50000


UnitAccess= namedtuple("UnitAccess",["id","nation","unitType"])


def generateUnitAccess(nationsCount, unitTypes):
    fake=Faker()
    rows=[]
    for i in range(accessCount):
        row=UnitAccess(i, random.randint(0,nationsCount), random.randint(0,unitTypes))
        rows.append(row)

    return rows


print(generateUnitAccess(100,10))