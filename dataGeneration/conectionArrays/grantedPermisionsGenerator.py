from collections import namedtuple
from faker import Faker
import random
from dataGeneration.config import *

# powinno być tyle co userów


Permission= namedtuple("Permission",["id","user","permission"])


def generateGrantedPermissions():
    userCount = USERS_COUNT
    fake=Faker()
    rows=[]
    for i in range(userCount):
        row=Permission(i, i, random.randint(0,PERM_COUNT-1))
        rows.append(row)

    return rows

