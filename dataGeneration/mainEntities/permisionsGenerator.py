from collections import namedtuple
from faker import Faker
import random
from dataGeneration.config import *



Permission= namedtuple("Permission",["id","name"])


def generatePermissionTypes():
    fake=Faker()
    permissions=[]
    for i in range(PERM_COUNT):
        permission=Permission(i, fake.unique.word())
        permissions.append(permission)

    return permissions


