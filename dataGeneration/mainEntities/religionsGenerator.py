from collections import namedtuple
from faker import Faker
import random

religionCount=100

Religion= namedtuple("Religion",["id","name"])


def generateReligions():
    fake=Faker()
    rows=[]
    for i in range(religionCount):
        row=Religion(i, fake.unique.word())
        rows.append(row)

    return rows


print(generateReligions())