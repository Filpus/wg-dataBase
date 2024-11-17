from collections import namedtuple
from faker import Faker
import random
from dataGeneration.config import *


UsedResource= namedtuple("UsedResource",["id","group","resource","amount"])


def generateUsedResource():
    resourceCount = RESOURCE_COUNT
    groupsCount = GROUP_COUNT
    groupResourcePairs=set()
    fake=Faker()
    rows=[]
    for i in range(USAGE_COUNT):
        k=0
        grp_res_pair=(random.randint(0,groupsCount-1), random.randint(0,resourceCount-1))
        while(groupResourcePairs.__contains__(grp_res_pair) or k<100):
            grp_res_pair=(random.randint(0,groupsCount-1), random.randint(0,resourceCount-1))
            k+=1

        if k==100: continue
        row=UsedResource(i, grp_res_pair[0],grp_res_pair[1], random.randint(1,50))
        rows.append(row)


    return rows


