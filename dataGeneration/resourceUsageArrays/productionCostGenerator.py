from collections import namedtuple
from faker import Faker
import random


costsCount=100
ProductionCost= namedtuple("ProductionCost",["id","unitType","resource","amount"])


def generateProductionCost(resourceCount,unitTypeCount):
    fake=Faker()
    rows=[]
    for i in range(costsCount):
        row=ProductionCost(i, random.randint(0,unitTypeCount), random.randint(0,resourceCount), random.randint(1,50))
        rows.append(row)


    return rows


print(generateProductionCost(50,50))