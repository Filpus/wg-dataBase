from collections import namedtuple
from faker import Faker
import random
from dataGeneration.config import *



TradeOffer= namedtuple("TradeOffer",["id","resource","agreement","amount"])


def generateWantedResource():
    resourceCount = RESOURCE_COUNT
    agreementsCount = AGREEMENT_COUNT
    fake=Faker()
    rows=[]
    for i in range(OFFER_COUNT):
        row=TradeOffer(i,  random.randint(0,resourceCount-1), random.randint(0,agreementsCount-1),random.randint(1,50))
        rows.append(row)


    return rows


