from collections import namedtuple
from faker import Faker
import random

resourceCount=100

Resource= namedtuple("Resource",["id","name","isMain"])


def generateResources():
    fake=Faker()
    rows=[]
    for i in range(resourceCount):
        row=Resource(i, fake.unique.word(), bool(random.randint(0,1)))
        rows.append(row)

    return rows


print(generateResources())