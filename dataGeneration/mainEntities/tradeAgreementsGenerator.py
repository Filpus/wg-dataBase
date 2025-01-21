from collections import namedtuple
from faker import Faker
import random
from dataGeneration.config import *



Agreement= namedtuple("Agreement",["nationOffering","nationAccepting","isAccepted","duration"])


def generateTrade():
    nationCount = NATIONS_COUNT
    fake=Faker()
    rows=[]
    for i in range(AGREEMENT_COUNT):
        nationOffering= random.randint(1,nationCount)
        nationAccepting= nationOffering+1 if nationOffering+1<nationCount else 0
        row=Agreement( nationOffering, nationAccepting,bool(random.randint(0,1)),random.randint(0,10))
        rows.append(row)

    return rows


