from collections import namedtuple
from faker import Faker
import random

permissionsCount=100

Permission= namedtuple("Permission",["id","name"])


def generatePermissions():
    fake=Faker()
    permissions=[]
    for i in range(permissionsCount):
        permission=Permission(i, fake.unique.word())
        permissions.append(permission)

    return permissions


print(generatePermissions())