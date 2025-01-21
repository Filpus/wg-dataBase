from collections import namedtuple
from faker import Faker
import random
from dataGeneration.config import *


costsCount=100
MaintenanceCost= namedtuple("MaintenanceCost",["unitType","resource","amount"])
existingMaintenaceCost = set()

def generateMaintenanceCosts():
    resourceCount = RESOURCE_COUNT
    unitTypeCount = UNIT_TYPE_COUNT
    fake=Faker()
    rows=[]
    for i in range(costsCount):
        row=MaintenanceCost( random.randint(1,unitTypeCount), random.randint(1,resourceCount), random.randint(1,50))
        maintenaceCost = row.unitType, row.resource
        if maintenaceCost not in existingMaintenaceCost:
            rows.append(row)
            existingMaintenaceCost.add(maintenaceCost)


    return rows


