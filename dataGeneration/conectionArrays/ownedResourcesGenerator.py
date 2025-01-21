from collections import namedtuple
from faker import Faker
import random
from dataGeneration.config import *



Ownership= namedtuple("Ownership",["nation","resource", "amount"])


def generateOwnerships():
    nationCount = NATIONS_COUNT
    resourceCount = RESOURCE_COUNT
    fake=Faker()
    rows=[]
    k=0
    for i in range(nationCount):
        for j in range(resourceCount):
            row=Ownership( i+1, j+1, random.randint(0,1000))
            rows.append(row)
            k+=1

    return rows


