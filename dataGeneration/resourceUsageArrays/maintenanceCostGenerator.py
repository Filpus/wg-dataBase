from collections import namedtuple
from faker import Faker
import random


costsCount=100
MaintenanceCost= namedtuple("MaintenanceCost",["id","unitType","resource","amount"])


def generateMaintenanceCosts(resourceCount,unitTypeCount):
    fake=Faker()
    rows=[]
    for i in range(costsCount):
        row=MaintenanceCost(i, random.randint(0,unitTypeCount), random.randint(0,resourceCount), random.randint(1,50))
        rows.append(row)


    return rows


print(generateMaintenanceCosts(50,50))