from collections import namedtuple
from faker import Faker
import random

permissionCount=50000


ResLoc= namedtuple("ResLoc",["id","location","resource","amount"])


def generateResourcesLoc(resourceCount,locationCount):
    fake=Faker()
    rows=[]
    for i in range(permissionCount):
        row=ResLoc(i, random.randint(0,locationCount), random.randint(0,resourceCount), random.randint(0,100))
        rows.append(row)

    return rows


print(generateResourcesLoc(3,500))