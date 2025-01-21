from collections import namedtuple
from faker import Faker
import random
from dataGeneration.config import *



NationAccess= namedtuple("NationAccess",["nation","user", "date","isActive"])


def generateNationAccess():
    nationsCount = NATIONS_COUNT
    usersCount = USERS_COUNT
    fake=Faker()
    activeAssigned=set()
    rows=[]
    for i in range(ACCESS_COUNT):
        row=NationAccess( random.randint(1,nationsCount), random.randint(1,usersCount),fake.date(),bool(random.randint(0,1)))
        if row.isActive and not activeAssigned.__contains__(row.nation):
            activeAssigned.add(row.nation)
        else:
            row=NationAccess( row.nation,row.user,row.date,False)
        rows.append(row)

    return rows

