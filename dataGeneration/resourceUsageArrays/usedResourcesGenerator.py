from collections import namedtuple
from faker import Faker
import random
from dataGeneration.config import *


UsedResource= namedtuple("UsedResource",["id","group","resource","amount"])


def generateUsedResource():
    resourceCount = RESOURCE_COUNT
    groupsCount = GROUP_COUNT
    fake=Faker()
    rows=[]
    for i in range(USAGE_COUNT):
        row=UsedResource(i, random.randint(0,groupsCount-1), random.randint(0,resourceCount-1), random.randint(1,50))
        rows.append(row)


    return rows


