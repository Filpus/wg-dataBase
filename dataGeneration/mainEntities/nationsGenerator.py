from collections import namedtuple
from faker import Faker
import random
from dataGeneration.config import *


Nation=namedtuple("Nation",  ["id","name","culture", "religion"])


def generateNations():
    cultureNum = CULTURE_COUNT
    religionNum = RELIGION_COUNT
    fake=Faker()
    nations=[]
    for i in range(NATIONS_COUNT):
        nation=Nation(i,fake.unique.country(),random.randint(0,cultureNum-1),random.randint(0,religionNum-1))
        nations.append(nation)

    return nations


