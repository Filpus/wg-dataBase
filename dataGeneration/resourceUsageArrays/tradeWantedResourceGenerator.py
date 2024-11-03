from collections import namedtuple
from faker import Faker
import random


offerCount=100
TradeOffer= namedtuple("TradeOffer",["id","resource","agreement","amount"])


def generateWantedResource(resourceCount,agreementsCount):
    fake=Faker()
    rows=[]
    for i in range(offerCount):
        row=TradeOffer(i,  random.randint(0,resourceCount), random.randint(0,agreementsCount),random.randint(1,50))
        rows.append(row)


    return rows


print(generateWantedResource(50,50))