from collections import namedtuple
from faker import Faker
import random
from dataGeneration.config import *




ResLoc= namedtuple("ResLoc",["location","resource","amount"])
existingResourcseInLocation = set()

def generateResourcesLoc():
    locationCount = LOCATION_COUNT
    resourceCount = RESOURCE_COUNT
    fake=Faker()
    rows=[]
    for i in range(LOC_RESOURCE_COUNT):
        row=ResLoc( random.randint(1,locationCount), random.randint(1,resourceCount), random.randint(0,100))
        resourceInLocation = row.resource, row.location
        if resourceInLocation not in existingResourcseInLocation:
            rows.append(row)
            existingResourcseInLocation.add(resourceInLocation)


    return rows


