from collections import namedtuple
from faker import Faker
import random
from dataGeneration.config import *


maxSpeed=10
minSpeed=1
maxMorale=20
minMorale=0
maxVolunteersNeeded=1000
maxDmg=20

UnitType= namedtuple("UnitType",["id","name","meleDmg","rangedDmg","defense","speed","morale","volunteersNeeded","isNaval"])


def generateUnitTypes():
    typesCount=UNIT_TYPE_COUNT
    fake=Faker()
    rows=[]
    for i in range(typesCount):
        row=UnitType(i, fake.unique.word(),random.randint(0,maxDmg),random.randint(0,maxDmg),random.randint(0,maxDmg),random.randint(minSpeed,maxSpeed),random.randint(minMorale,maxMorale),random.randint(100,maxVolunteersNeeded), bool(random.randint(0,1)))
        rows.append(row)

    return rows


