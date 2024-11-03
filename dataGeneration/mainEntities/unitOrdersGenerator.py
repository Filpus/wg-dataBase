from collections import namedtuple
from faker import Faker
import random
from dataGeneration.config import *



Order= namedtuple("Order",["id","nation","unitType","quantity"])
existingOrders=set()

def generateOrders():
    nationsCount = NATIONS_COUNT
    unitTypes = UNIT_TYPE_COUNT

    fake=Faker()
    rows=[]
    for i in range(ORDERS_COUNT):
        row=Order(i, random.randint(0,nationsCount-1), random.randint(0,unitTypes-1), random.randint(MIN_TROOPS_QUANTITY,MAX_TROOPS_QUANTITY))
        if (row.nation,row.unitType) not in existingOrders:
            existingOrders.add((row.nation,row.unitType))
            rows.append(row)

    return rows


