from collections import namedtuple
from faker import Faker
import random
from dataGeneration.config import *


costsCount=100
ProductionCost= namedtuple("ProductionCost",["id","unitType","resource","amount"])


def generateProductionCost():

    fake=Faker()
    rows=[]
    for i in range(costsCount):
        row=ProductionCost(i, random.randint(0, UNIT_TYPE_COUNT-1), random.randint(0,RESOURCE_COUNT-1), random.randint(1,50))
        rows.append(row)


    return rows


