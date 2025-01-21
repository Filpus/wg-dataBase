from collections import namedtuple
from faker import Faker
import random
from dataGeneration.config import *

sharesCount=100
ProductionShare= namedtuple("ProductionShare",["group","resource","coef"])
existingProductionShare = set()

def generateProductionShare():
    resourceCount = RESOURCE_COUNT
    groupsCount = GROUP_COUNT
    fake=Faker()
    rows=[]
    for i in range(sharesCount):
        row=ProductionShare( random.randint(1,groupsCount), random.randint(1,resourceCount), random.randint(1,50))
        productionShare = row.group,row.resource
        if productionShare not in existingProductionShare:
            rows.append(row)
            existingProductionShare.add(productionShare)

    return rows


