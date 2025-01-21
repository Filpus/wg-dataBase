from collections import namedtuple
from faker import Faker
import random
from dataGeneration.config import *



Culture= namedtuple("Culture",  ["name"])


def generateCulture():
    fake=Faker()
    cultures=[]
    for i in range(CULTURE_COUNT):
        culture=Culture(fake.unique.word())
        cultures.append(culture)

    return cultures


