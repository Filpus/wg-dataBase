from collections import namedtuple
from faker import Faker
import random

armiesCount=10000

Army= namedtuple("Army",  ["id","name", "nation","location"])


def generateArmies(nationNum, locationNum):
    fake=Faker()
    armies=[]
    for i in range(armiesCount):
        army=Army(i,fake.word(),random.randint(0,nationNum),random.randint(0,locationNum))
        armies.append(army)

    return armies


print(generateArmies(200,10000))