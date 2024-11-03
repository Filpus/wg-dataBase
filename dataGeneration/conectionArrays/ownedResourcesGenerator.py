from collections import namedtuple
from faker import Faker
import random



Ownership= namedtuple("Ownership",["id","nation","resource", "amount"])


def generateOwnerships(nationCount,resourceCount):
    fake=Faker()
    rows=[]
    for i in range(nationCount):
        for j in range(resourceCount):
            row=Ownership(i, i, j, random.randint(0,1000))
            rows.append(row)

    return rows


print(generateOwnerships(200,50))