from collections import namedtuple
from faker import Faker
import random

permissionCount=30 # powinno być tyle co userów


Permission= namedtuple("Permission",["id","user","permission"])


def generatePermissions(permCount):
    fake=Faker()
    rows=[]
    for i in range(permissionCount):
        row=Permission(i, i, random.randint(0,permCount))
        rows.append(row)

    return rows


print(generatePermissions(3))