from collections import namedtuple
from faker import Faker
import random
from dataGeneration.config import *


Nation=namedtuple("Nation",  ["name","culture", "religion"])


def generateNations():
    cultureNum = CULTURE_COUNT
    religionNum = RELIGION_COUNT
    fake=Faker()
    nations=[]
    for i in range(NATIONS_COUNT):
        nation=Nation(fake.unique.country(),random.randint(1,cultureNum),random.randint(1,religionNum))
        nations.append(nation)

    return nations


