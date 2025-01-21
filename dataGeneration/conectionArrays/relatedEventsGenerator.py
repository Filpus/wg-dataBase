from collections import namedtuple
from faker import Faker
import random
from dataGeneration.config import *


RelatedEvent= namedtuple("RelatedEvent",["nation","event"])
existingRelatedEvents = set()

def generateRelatedEvents():
    eventCount = EVENT_COUNT
    nationCount = NATIONS_COUNT
    fake=Faker()
    rows=[]
    for i in range(RELATED_EVENTS_COUNT):
        row=RelatedEvent( random.randint(1,nationCount), random.randint(1,eventCount))
        related = row.nation, row.event
        if related not in existingRelatedEvents:
            rows.append(row)
            existingRelatedEvents.add(related)

    return rows


