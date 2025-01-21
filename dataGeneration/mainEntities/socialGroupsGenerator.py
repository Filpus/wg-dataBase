from collections import namedtuple
from faker import Faker
import random
from dataGeneration.config import *


Group= namedtuple("Group",["name","baseSatisfaction","volunteers"])


def generateSocialGroups():
    fake=Faker()
    rows=[]
    for i in range(GROUP_COUNT):
        row=Group( fake.unique.word(),float(random.randint(0,100)/100),random.randint(0,MAX_VOLUNTEERS_NUMBER) )
        rows.append(row)

    return rows


