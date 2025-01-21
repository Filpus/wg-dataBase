from collections import namedtuple
from faker import Faker
import random
from dataGeneration.config import *



TradeOffer= namedtuple("TradeOffer",["resource","agreement","amount"])


def generateTradeOffer():
    resourceCount = RESOURCE_COUNT
    agreementsCount = AGREEMENT_COUNT
    fake=Faker()
    rows=[]
    for i in range(OFFER_COUNT):
        row=TradeOffer(  random.randint(1,resourceCount), random.randint(1,agreementsCount),random.randint(1,50))
        rows.append(row)


    return rows


