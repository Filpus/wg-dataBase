from collections import namedtuple
from faker import Faker
import random

nationCount=200

Nation=namedtuple("Nation",  ["id","name","culture", "religion"])


def generateNations(cultureNum, religionNum):
    fake=Faker()
    nations=[]
    for i in range(nationCount):
        nation=Nation(i,fake.unique.country(),random.randint(0,cultureNum),random.randint(0,religionNum))
        nations.append(nation)

    return nations


#print(generateNations(10,10))