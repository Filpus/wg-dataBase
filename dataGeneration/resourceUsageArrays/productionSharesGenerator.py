from collections import namedtuple
from faker import Faker
import random
from dataGeneration.config import *


sharesCount=100
ProductionShare= namedtuple("ProductionShare",["id","group","resource","coef"])


def generateProductionShare():
    resourceCount = RESOURCE_COUNT
    groupsCount = GROUP_COUNT
    fake=Faker()
    rows=[]
    for i in range(sharesCount):
        row=ProductionShare(i, random.randint(0,groupsCount-1), random.randint(0,resourceCount-1), random.randint(1,50))
        rows.append(row)


    return rows


