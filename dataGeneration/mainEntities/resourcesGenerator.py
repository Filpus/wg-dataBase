from collections import namedtuple
from faker import Faker
import random
from dataGeneration.config import *

resourceCount=100

Resource= namedtuple("Resource",["name","isMain"])


def generateResources():
    fake=Faker()
    rows=[]
    for i in range(RESOURCE_COUNT):
        row=Resource( fake.unique.word(), bool(random.randint(0,1)))
        rows.append(row)

    return rows


