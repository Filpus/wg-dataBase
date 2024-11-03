from collections import namedtuple
from faker import Faker
import random
from dataGeneration.config import *




ResLoc= namedtuple("ResLoc",["id","location","resource","amount"])


def generateResourcesLoc():
    locationCount = LOCATION_COUNT
    resourceCount = RESOURCE_COUNT
    fake=Faker()
    rows=[]
    for i in range(LOC_RESOURCE_COUNT):
        row=ResLoc(i, random.randint(0,locationCount-1), random.randint(0,resourceCount-1), random.randint(0,100))
        rows.append(row)

    return rows


