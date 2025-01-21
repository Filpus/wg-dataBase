from collections import namedtuple
from faker import Faker
import random
from dataGeneration.config import *



Permission= namedtuple("Permission",["name"])


def generatePermissionTypes():
    fake=Faker()
    permissions=[]
    for i in range(PERM_COUNT):
        permission=Permission( fake.unique.word())
        permissions.append(permission)

    return permissions


