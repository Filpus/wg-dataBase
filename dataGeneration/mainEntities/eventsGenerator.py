from collections import namedtuple
from faker import Faker
import random
from dataGeneration.config import *



Event= namedtuple("Event",["name", "description"])


def generateEvents():
    fake=Faker()
    events=[]
    for i in range(EVENT_COUNT):
        event=Event(fake.word(),fake.text())
        events.append(event)

    return events


