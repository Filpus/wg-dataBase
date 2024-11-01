from collections import namedtuple
from faker import Faker
import random

actionCount=10000

Action= namedtuple("Action",  ["id","nation","name", "description","result","isSettled"])


def generateActions(nationNum):
    fake=Faker()
    actions=[]
    for i in range(actionCount):
        action=Action(i,fake.word(),random.randint(0,nationNum),fake.text(),fake.text(),bool(random.randint(0,1)))
        actions.append(action)

    return actions


print(generateActions(200))