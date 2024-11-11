from collections import namedtuple
from faker import Faker
import random
from dataGeneration.config import *

# powinno być tyle co userów


Permission= namedtuple("Permission",["id","user","permission"])
existingPermisions = set()

def generateGrantedPermissions():
    userCount = USERS_COUNT
    fake=Faker()
    rows=[]
    for i in range(userCount):
        row=Permission(i, i, random.randint(0,PERM_COUNT-1))
        permisions = row.user, row.permission
        if permisions not in existingPermisions:
            rows.append(row)
            existingPermisions.add(permisions)

    return rows

