from collections import namedtuple
from faker import Faker
import random

popCount=100

Pop= namedtuple("Pop",["id","name"])


def generatePermissions():
    fake=Faker()
    pops=[]
    for i in range(popCount):
        pop=Pop(i, fake.unique.word())
        pops.append(pop)

    return pops


print(generatePermissions())