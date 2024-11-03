from collections import namedtuple
from faker import Faker
import random


usageCount=100
UsedResource= namedtuple("UsedResource",["id","group","resource","amount"])


def generateUsedResource(resourceCount,groupsCount):
    fake=Faker()
    rows=[]
    for i in range(usageCount):
        row=UsedResource(i, random.randint(0,groupsCount), random.randint(0,resourceCount), random.randint(1,50))
        rows.append(row)


    return rows


print(generateUsedResource(50,50))