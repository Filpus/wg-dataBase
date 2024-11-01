from collections import namedtuple
from faker import Faker
import random

eventsCount=100

Event= namedtuple("Event",["id","name", "description"])


def generateEvents():
    fake=Faker()
    events=[]
    for i in range(eventsCount):
        event=Event(i,fake.word(),fake.text())
        events.append(event)

    return events


print(generateEvents())