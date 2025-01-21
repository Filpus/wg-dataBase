from collections import namedtuple
from faker import Faker
import random
from dataGeneration.config import *



Order= namedtuple("Order",["nation","unitType","quantity"])
existingOrders=set()

def generateOrders():
    nationsCount = NATIONS_COUNT
    unitTypes = UNIT_TYPE_COUNT

    fake=Faker()
    rows=[]
    for i in range(ORDERS_COUNT):
        row=Order( random.randint(1,nationsCount), random.randint(1,unitTypes), random.randint(MIN_TROOPS_QUANTITY,MAX_TROOPS_QUANTITY))
        if (row.nation,row.unitType) not in existingOrders:
            existingOrders.add((row.nation,row.unitType))
            rows.append(row)

    return rows


