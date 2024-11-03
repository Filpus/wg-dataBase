from collections import namedtuple
from faker import Faker
import random

troopsCount=100
maxTroopsQuantity= 10000
minTroopsQuantity=100

Troops= namedtuple("Troops",["id","quantity","army","unitType"])


def generateTroops(armiesCount, unitTypes):
    fake=Faker()
    rows=[]
    for i in range(troopsCount):
        row=Troops(i, random.randint(minTroopsQuantity,maxTroopsQuantity), random.randint(0,armiesCount), random.randint(0,unitTypes))
        rows.append(row)

    return rows


print(generateTroops(100,10))