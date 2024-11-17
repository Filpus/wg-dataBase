from collections import namedtuple
from faker import Faker
import random
from dataGeneration.config import *



NationAccess= namedtuple("NationAccess",["id","nation","user", "date","isActive"])


def generateNationAccess():
    nationsCount = NATIONS_COUNT
    usersCount = USERS_COUNT
    fake=Faker()
    activeAssigned=set()
    rows=[]
    for i in range(ACCESS_COUNT):
        row=NationAccess(i, random.randint(0,nationsCount-1), random.randint(0,usersCount-1),fake.date(),bool(random.randint(0,1)))
        if row.isActive and not activeAssigned.__contains__(row.nation):
            activeAssigned.add(row.nation)
        else:
            row=NationAccess(i, row.nation,row.user,row.date,False)
        rows.append(row)

    return rows

