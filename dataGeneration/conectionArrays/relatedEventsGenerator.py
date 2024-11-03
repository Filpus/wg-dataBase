from collections import namedtuple
from faker import Faker
import random
from dataGeneration.config import *


RelatedEvent= namedtuple("RelatedEvent",["id","nation","event"])


def generateRelatedEvents():
    eventCount = EVENT_COUNT
    nationCount = NATIONS_COUNT
    fake=Faker()
    rows=[]
    for i in range(RELATED_EVENTS_COUNT):
        row=RelatedEvent(i, random.randint(0,nationCount-1), random.randint(0,eventCount-1))
        rows.append(row)

    return rows


