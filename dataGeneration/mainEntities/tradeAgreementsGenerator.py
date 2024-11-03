from collections import namedtuple
from faker import Faker
import random
from dataGeneration.config import *



Agreement= namedtuple("Agreement",["id","nationOffering","nationAccepting","isAccepted"])


def generateTrade():
    nationCount = NATIONS_COUNT
    fake=Faker()
    rows=[]
    for i in range(AGREEMENT_COUNT):
        nationOffering= random.randint(0,nationCount-1)
        nationAccepting= nationOffering+1 if nationOffering+1<nationCount else 0
        row=Agreement(i, nationOffering, nationAccepting,bool(random.randint(0,1)))
        rows.append(row)

    return rows


