from collections import namedtuple
from faker import Faker
import random
from dataGeneration.config import *



Religion= namedtuple("Religion",["name"])


def generateReligions():
    fake=Faker()
    rows=[]
    for i in range(RELIGION_COUNT):
        row=Religion( fake.unique.word())
        rows.append(row)

    return rows


