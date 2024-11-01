from collections import namedtuple
from faker import Faker
import random

cultureCount=50

Culture= namedtuple("Culture",  ["id","name"])


def generateCulture():
    fake=Faker()
    cultures=[]
    for i in range(cultureCount):
        culture=Culture(i,fake.unique.word())
        cultures.append(culture)

    return cultures


print(generateCulture())