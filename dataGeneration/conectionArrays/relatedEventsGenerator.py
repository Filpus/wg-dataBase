from collections import namedtuple
from faker import Faker
import random

relatedEventsCount=100
RelatedEvent= namedtuple("RelatedEvent",["id","nation","event"])


def generateRelatedEvents(nationCount,eventCount):
    fake=Faker()
    rows=[]
    for i in range(relatedEventsCount):
        row=RelatedEvent(i, random.randint(0,nationCount), random.randint(0,eventCount))
        rows.append(row)

    return rows


print(generateRelatedEvents(200,500))