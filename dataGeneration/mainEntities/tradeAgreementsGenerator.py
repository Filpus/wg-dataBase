from collections import namedtuple
from faker import Faker
import random

agreementCount=100

Agreement= namedtuple("Agreement",["id","nationOffering","nationAccepting","isAccepted"])


def generateSocialGroups(nationCount):
    fake=Faker()
    rows=[]
    for i in range(agreementCount):
        nationOffering= random.randint(0,nationCount)
        nationAccepting= nationOffering+1 if nationOffering+1<nationCount else 0
        row=Agreement(i, nationOffering, nationAccepting,bool(random.randint(0,1)))
        rows.append(row)

    return rows


print(generateSocialGroups(100))