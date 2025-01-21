from collections import namedtuple
from faker import Faker
import random
from dataGeneration.config import *



Action= namedtuple("Action",  ["nation","name", "description","result","isSettled"])


def generateActions():
    nationNum = NATIONS_COUNT
    fake=Faker()
    actions=[]
    for i in range(ACTION_COUNT):
        action=Action(random.randint(1,nationNum),fake.word(),fake.text(),fake.text(),bool(random.randint(0,1)))
        actions.append(action)

    return actions


