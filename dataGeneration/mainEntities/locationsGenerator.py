from collections import namedtuple
from faker import Faker
import random

locationsCount=1000
maxLocationSize=100
maxFortificationSize=10

namedtuple("location",["id","name", "size","fortifications","nation"])


def generateLocations(nationsCount):
    fake=Faker()
    locations=[]
    for i in range(locationsCount):
        location=(i,fake.word(),random.randint(1,maxLocationSize),random.randint(1,maxFortificationSize),random.randint(1,nationsCount))
        locations.append(location)

    return locations


print(generateLocations(200))