from collections import namedtuple
from faker import Faker
import random
from dataGeneration.config import *



UnitAccess= namedtuple("UnitAccess",["id","nation","user", "date","isActive"])


def generateNationAccess():
    nationsCount = NATIONS_COUNT
    usersCount = USERS_COUNT
    fake=Faker()
    rows=[]
    for i in range(ACCESS_COUNT):
        row=UnitAccess(i, random.randint(0,nationsCount-1), random.randint(0,usersCount-1),fake.date(),bool(random.randint(0,1)))
        rows.append(row)

    return rows

