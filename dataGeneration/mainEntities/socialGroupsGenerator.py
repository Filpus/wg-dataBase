from collections import namedtuple
from faker import Faker
import random

groupsCount=100
maxVolunteersNumber =1000

Group= namedtuple("Group",["id","name","baseSatisfaction","volunteers"])


def generateSocialGroups():
    fake=Faker()
    rows=[]
    for i in range(groupsCount):
        row=Group(i, fake.unique.word(),float(random.randint(0,100)/100),random.randint(0,maxVolunteersNumber) )
        rows.append(row)

    return rows


print(generateSocialGroups())