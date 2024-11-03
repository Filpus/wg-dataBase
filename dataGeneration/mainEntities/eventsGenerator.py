from collections import namedtuple
from faker import Faker
import random
from dataGeneration.config import *



Event= namedtuple("Event",["id","name", "description"])


def generateEvents():
    fake=Faker()
    events=[]
    for i in range(EVENT_COUNT):
        event=Event(i,fake.word(),fake.text())
        events.append(event)

    return events


