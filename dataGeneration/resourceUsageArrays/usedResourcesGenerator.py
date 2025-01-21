from collections import namedtuple
from faker import Faker
import random
from dataGeneration.config import *


UsedResource= namedtuple("UsedResource",["group","resource","amount"])
existingUsedResources = set()

def generateUsedResource():
    resourceCount = RESOURCE_COUNT
    groupsCount = GROUP_COUNT
    groupResourcePairs=set()
    fake=Faker()
    rows=[]
    for i in range(USAGE_COUNT):
        k=0
        grp_res_pair=(random.randint(1,groupsCount), random.randint(1,resourceCount))
        while(groupResourcePairs.__contains__(grp_res_pair) or k<100):
            grp_res_pair=(random.randint(1,groupsCount), random.randint(1,resourceCount))
            k+=1

        if k==100: continue
        row=UsedResource( grp_res_pair[0],grp_res_pair[1], random.randint(1,50))

        ur = row.resource, row.group
        if ur not in existingUsedResources:
            rows.append(row)
            existingUsedResources.add(ur)

    return rows


