from collections import namedtuple
from faker import Faker
import random
from dataGeneration.config import *


costsCount=100
ProductionCost= namedtuple("ProductionCost",["unitType","resource","amount"])
existingProductionCost = set()

def generateProductionCost():

    fake=Faker()
    rows=[]
    for i in range(costsCount):
        row=ProductionCost(random.randint(1, UNIT_TYPE_COUNT), random.randint(1,RESOURCE_COUNT), random.randint(1,50))
        productionCost = row.unitType, row.resource
        if productionCost not in existingProductionCost:
            rows.append(row)
            existingProductionCost.add(productionCost)

    return rows


