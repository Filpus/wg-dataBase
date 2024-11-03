from collections import namedtuple
from faker import Faker
import random


sharesCount=100
ProductionShare= namedtuple("ProductionShare",["id","group","resource","coef"])


def generateProductionShare(resourceCount,groupsCount):
    fake=Faker()
    rows=[]
    for i in range(sharesCount):
        row=ProductionShare(i, random.randint(0,groupsCount), random.randint(0,resourceCount), random.randint(1,50))
        rows.append(row)


    return rows


print(generateProductionShare(50,50))