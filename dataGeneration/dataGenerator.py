#script running all other generation scripts

import psycopg2

from dataGeneration.mainEntities.religionsGenerator import generateReligions

# Connect to PostgreSQL database
connection = psycopg2.connect(
    host="localhost",
    database="wg",
    user="postgres",
    password="admin"
)
cursor = connection.cursor()


accessestonations_query = '''INSERT INTO accessestonations (id, fk_nations,fk_users) VALUES (%s, %s,%s, %s,%s);'''
accessestounits_query = '''INSERT INTO accessestounits (id,fk_nations, fk_unittypes ) VALUES (%s, %s,%s);'''
actions_query = '''INSERT INTO actions (id, fk_nations,name,description,result,issettled) VALUES (%s, %s,%s,%s, %s,%s);'''
armies_query = '''INSERT INTO armies (id, name, fk_nations, fk_locations) VALUES (%s, %s,%s, %s);'''
cultures_query = '''INSERT INTO cultures (id, name) VALUES (%s, %s);'''
events_query = '''INSERT INTO events (id, name,description) VALUES (%s, %s, %s);'''
grantedpermissions_query = '''INSERT INTO grantedpermissions (id, fk_users, fk_permissions) VALUES (%s, %s,%s);'''
locationresources_query = '''INSERT INTO locationresources (id, fk_locations, fk_resources,amount) VALUES (%s, %s,%s, %s);'''
locations_query = '''INSERT INTO locations (id, name,size,fortifications,fk_nations) VALUES (%s, %s,%s, %s,%s);'''
maintenancecosts_query = '''INSERT INTO maintenancecosts (id, fk_unittypes,fk_resources,amount) VALUES (%s, %s,%s, %s);'''
modifiers_query = '''INSERT INTO modifiers (id, fk_events,target,fk_resources,fk_socialgroups,fk_cultures,fk_religions) VALUES (%s, %s,%s, %s,%s, %s,%s);'''
nations_query = '''INSERT INTO nations (id, name,fk_cultures,fk_religions) VALUES (%s, %s,%s, %s);'''
offeredresources_query = '''INSERT INTO offeredresources (id, fk_resources,fk_tradeagreement, amount) VALUES (%s, %s,%s, %s);'''
ownedresources_query = '''INSERT INTO ownedresources (id, fk_nations, fk_resources,ammount) VALUES (%s, %s,%s, %s);'''
permissions_query = '''INSERT INTO permissions (id, name) VALUES (%s, %s);'''
populations_query = '''INSERT INTO populations (id, fk_socialgroups, fk_cultures, fk_religions, fk_locations, satosfaction) VALUES (%s, %s,%s, %s,%s, %s);'''
productioncosts_query = '''INSERT INTO productioncosts (id, fk_unitytyoes, fk_resources, amount) VALUES (%s, %s,%s, %s);'''
productionshares_query = '''INSERT INTO productionshares (id, fk_socialgroups, fk_resources, coefficient) VALUES (%s, %s,%s, %s);'''
relatedevents_query = '''INSERT INTO relatedevents (id, fk_nations, fk_events) VALUES (%s, %s,%s);'''
religion_query = '''INSERT INTO religions (id, name) VALUES (%s, %s);'''
resources_query = '''INSERT INTO resources (id, name, ismain) VALUES (%s, %s,%s);'''
socialgroups_query = '''INSERT INTO socialgroups (id, name, basesatisfaction, volunteers) VALUES (%s, %s,%s, %s);'''
tradeagreements_query = '''INSERT INTO tradeagreements (id, fk_nationoffering, fk_nationreceiving,isaccepted) VALUES (%s, %s,%s, %s);'''
troops_query = '''INSERT INTO troops (id, quantity, fk_armies, fk_unittypes) VALUES (%s, %s,%s, %s);'''
unitorders_query = '''INSERT INTO unitorders (id, fk_nations, fk_unittypes, quantity) VALUES (%s, %s,%s, %s);'''
unittypes_query = '''INSERT INTO unittypes (id, name,mele, range,speed,morale,volunteersneeded,isnaval) VALUES (%s, %s,%s, %s,%s, %s,%s, %s);'''
usedresources_query = '''INSERT INTO usedresources  (id, fk_socialgroups,fk_resources,amount) VALUES (%s, %s,%s, %s);'''
users_query = '''INSERT INTO users (id, name,email,password,isarchived) VALUES (%s, %s,%s, %s,%s);'''
wantedresources_query = '''INSERT INTO wantedresources (id, fk_resources,fk_tradeagreements,amount) VALUES (%s, %s,%s, %s);'''

# Convert data into tuples
records = generateReligions()
insert_query=religion_query
# Insert data in batch
cursor.executemany(insert_query, records)
connection.commit()

cursor.close()
connection.close()