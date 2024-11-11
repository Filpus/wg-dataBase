from collections import namedtuple
from faker import Faker
import random
from dataGeneration.config import *


RelatedEvent= namedtuple("RelatedEvent",["id","nation","event"])
existingRelatedEvents = set()

def generateRelatedEvents():
    eventCount = EVENT_COUNT
    nationCount = NATIONS_COUNT
    fake=Faker()
    rows=[]
    for i in range(RELATED_EVENTS_COUNT):
        row=RelatedEvent(i, random.randint(0,nationCount-1), random.randint(0,eventCount-1))
        related = row.nation, row.event
        if related not in existingRelatedEvents:
            rows.append(row)
            existingRelatedEvents.add(related)

    return rows


