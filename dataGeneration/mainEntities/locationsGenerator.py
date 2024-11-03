from collections import namedtuple
from faker import Faker
import random
from dataGeneration.config import *


namedtuple("location",["id","name", "size","fortifications","nation"])


def generateLocations():
    nationsCount = NATIONS_COUNT

    fake=Faker()
    locations=[]
    for i in range(LOCATION_COUNT):
        location=(i,fake.unique.word(),random.randint(1,MAX_LOCATION_SIZE),random.randint(1,MAX_FORTIFICATION_SIZE),random.randint(1,nationsCount-1))
        locations.append(location)

    return locations


