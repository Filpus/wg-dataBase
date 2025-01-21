from collections import namedtuple
from faker import Faker
import random
from dataGeneration.config import *

# powinno być tyle co userów


Permission= namedtuple("Permission",["user","permission"])
existingPermisions = set()

def generateGrantedPermissions():
    userCount = USERS_COUNT
    fake=Faker()
    rows=[]
    for i in range(userCount):
        row=Permission( i+1, random.randint(1,PERM_COUNT))
        permisions = row.user, row.permission
        if permisions not in existingPermisions:
            rows.append(row)
            existingPermisions.add(permisions)

    return rows

