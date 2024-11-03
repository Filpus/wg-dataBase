from collections import namedtuple
from faker import Faker
import random
import bcrypt

usersCount=30


User= namedtuple("User",["id","name","email","password","isArchived"])
domains=["gmail.com", "wp.pl", "onet.pl"]

def generateUsers():
    fake=Faker()
    rows=[]
    for i in range(usersCount):
        row=User(i, fake.name(), fake.email(True, random.choice(domains)),bcrypt.hashpw(fake.password().encode(),bcrypt.gensalt()),bool(random.randint(0,1)) )
        rows.append(row)

    return rows


print(generateUsers())