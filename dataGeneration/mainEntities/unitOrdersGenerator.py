from collections import namedtuple
from faker import Faker
import random

ordersCount=50000
maxTroopsQuantity= 10000
minTroopsQuantity=100

Order= namedtuple("Order",["id","nation","unitType","quantity"])


def generateOrders(nationsCount, unitTypes):
    fake=Faker()
    rows=[]
    for i in range(ordersCount):
        row=Order(i, random.randint(0,nationsCount), random.randint(0,unitTypes), random.randint(minTroopsQuantity,maxTroopsQuantity))
        rows.append(row)

    return rows


print(generateOrders(100,10))