#script running all other generation scripts

import psycopg2

from dataGeneration.conectionArrays.accessToNationsGenerator import generateNationAccess
from dataGeneration.conectionArrays.grantedPermisionsGenerator import generateGrantedPermissions
from dataGeneration.conectionArrays.locationResourcesGenerator import generateResourcesLoc
from dataGeneration.conectionArrays.ownedResourcesGenerator import generateOwnerships
from dataGeneration.conectionArrays.relatedEventsGenerator import generateRelatedEvents
from dataGeneration.conectionArrays.unitAccesGenerator import generateUnitAccess
from dataGeneration.mainEntities.actionsGenerator import generateActions
from dataGeneration.mainEntities.armiesGenerator import generateArmies
from dataGeneration.mainEntities.culturesGenerator import generateCulture
from dataGeneration.mainEntities.eventsGenerator import generateEvents
from dataGeneration.mainEntities.locationsGenerator import generateLocations
from dataGeneration.mainEntities.modifiersGenerator import generateModifiers
from dataGeneration.mainEntities.nationsGenerator import generateNations
from dataGeneration.mainEntities.permisionsGenerator import generatePermissionTypes, generatePermissionTypes
from dataGeneration.mainEntities.popGenerator import generatePops
from dataGeneration.mainEntities.religionsGenerator import generateReligions
from dataGeneration.mainEntities.resourcesGenerator import generateResources
from dataGeneration.mainEntities.socialGroupsGenerator import generateSocialGroups
from dataGeneration.mainEntities.tradeAgreementsGenerator import generateTrade
from dataGeneration.mainEntities.troopsGenerator import generateTroops
from dataGeneration.mainEntities.unitOrdersGenerator import generateOrders
from dataGeneration.mainEntities.unitTypesGenerator import generateUnitTypes
from dataGeneration.mainEntities.usersGenerator import generateUsers
from dataGeneration.resourceUsageArrays.maintenanceCostGenerator import generateMaintenanceCosts
from dataGeneration.resourceUsageArrays.productionCostGenerator import generateProductionCost
from dataGeneration.resourceUsageArrays.productionSharesGenerator import generateProductionShare
from dataGeneration.resourceUsageArrays.tradeOfferedResourcesGenerator import generateTradeOffer
from dataGeneration.resourceUsageArrays.tradeWantedResourceGenerator import generateWantedResource
from dataGeneration.resourceUsageArrays.usedResourcesGenerator import generateUsedResource

# Connect to PostgreSQL database
connection = psycopg2.connect(
    host="localhost",
    database="wg",
    user="postgres",
    password="admin"
)
cursor = connection.cursor()


# Encje silne
cultures_query = '''INSERT INTO cultures (id, name) VALUES (%s, %s);'''
religions_query = '''INSERT INTO religions (id, name) VALUES (%s, %s);'''
resources_query = '''INSERT INTO resources (id, name, ismain) VALUES (%s, %s,%s);'''
socialgroups_query = '''INSERT INTO socialgroups (id, name, basesatisfaction, volunteers) VALUES (%s, %s,%s, %s);'''
users_query = '''INSERT INTO users (id, name,email,password,isarchived) VALUES (%s, %s,%s, %s,%s);'''
unittypes_query = '''INSERT INTO unittypes (id, name,melee, range,speed,morale,volunteersneeded,isnaval) VALUES (%s, %s,%s, %s,%s, %s,%s, %s);'''

# Encje zależne
nations_query = '''INSERT INTO nations (id, name,fk_cultures,fk_religions) VALUES (%s, %s,%s, %s);'''
locations_query = '''INSERT INTO locations (id, name,size,fortifications,fk_nations) VALUES (%s, %s,%s, %s,%s);'''
accessestonations_query = '''INSERT INTO accessestonations (id, fk_nations,fk_users,dateacquired,isactive) VALUES (%s, %s,%s, %s,%s);'''
accessestounits_query = '''INSERT INTO accessestounits (id,fk_nations, fk_unittypes ) VALUES (%s, %s,%s);'''
actions_query = '''INSERT INTO actions (id, fk_nations,name,description,result,issettled) VALUES (%s, %s,%s,%s, %s,%s);'''
armies_query = '''INSERT INTO armies (id, name, fk_nations, fk_locations) VALUES (%s, %s,%s, %s);'''
events_query = '''INSERT INTO events (id, name,description) VALUES (%s, %s, %s);'''
grantedpermissions_query = '''INSERT INTO grantedpermissions (id, fk_users, fk_permissions) VALUES (%s, %s,%s);'''
locationresources_query = '''INSERT INTO locationresources (id, fk_locations, fk_resources,amount) VALUES (%s, %s,%s, %s);'''
maintenancecosts_query = '''INSERT INTO maintenancecosts (id, fk_unittypes,fk_resources,amount) VALUES (%s, %s,%s, %s);'''
modifiers_query = '''INSERT INTO modifiers (id, fk_events,target,fk_resources,fk_socialgroups,fk_cultures,fk_religions) VALUES (%s, %s,%s, %s,%s, %s,%s);'''
offeredresources_query = '''INSERT INTO offeredresources (id, fk_resources,fk_tradeagreements, amount) VALUES (%s, %s,%s, %s);'''
ownedresources_query = '''INSERT INTO ownedresources (id, fk_nations, fk_resources,amount) VALUES (%s, %s,%s, %s);'''
permissions_query = '''INSERT INTO permissions (id, name) VALUES (%s, %s);'''
populations_query = '''INSERT INTO populations (id, fk_socialgroups, fk_cultures, fk_religions, fk_locations, satisfaction) VALUES (%s, %s,%s, %s,%s, %s);'''
productioncosts_query = '''INSERT INTO productioncosts (id, fk_unittypes, fk_resources, amount) VALUES (%s, %s,%s, %s);'''
productionshares_query = '''INSERT INTO productionshares (id, fk_socialgroups, fk_resources, coefficient) VALUES (%s, %s,%s, %s);'''
relatedevents_query = '''INSERT INTO relatedevents (id, fk_nations, fk_events) VALUES (%s, %s,%s);'''
tradeagreements_query = '''INSERT INTO tradeagreements (id, fk_nationoffering, fk_nationreceiving,isaccepted) VALUES (%s, %s,%s, %s);'''
troops_query = '''INSERT INTO troops (id, quantity, fk_armies, fk_unittypes) VALUES (%s, %s,%s, %s);'''
unitorders_query = '''INSERT INTO unitorders (id, fk_nations, fk_unittypes, quantity) VALUES (%s, %s,%s, %s);'''
usedresources_query = '''INSERT INTO usedresources  (id, fk_socialgroups,fk_resources,amount) VALUES (%s, %s,%s, %s);'''
wantedresources_query = '''INSERT INTO wantedresources (id, fk_resources,fk_tradeagreements,amount) VALUES (%s, %s,%s, %s);'''



queryList= [
    cultures_query,
    religions_query,
    nations_query,
    resources_query,
    locations_query,
    socialgroups_query,
    users_query,
    unittypes_query,
    accessestonations_query,
    accessestounits_query,
    actions_query,
    armies_query,
    events_query,
    permissions_query,
    grantedpermissions_query,
    locationresources_query,
    maintenancecosts_query,
    modifiers_query,
    tradeagreements_query,
    offeredresources_query,
    ownedresources_query,
    populations_query,
    productioncosts_query,
    productionshares_query,
    relatedevents_query,
    troops_query,
    unitorders_query,
    usedresources_query,
    wantedresources_query
]

functionsList = [
    generateCulture,          # cultures_query
    generateReligions,        # religion_query
    generateNations,          # nations_query
    generateResources,        # resources_query
    generateLocations,        # locations_query
    generateSocialGroups,      # socialgroups_query
    generateUsers,            # users_query
    generateUnitTypes,        # unittypes_query
    generateNationAccess,     # accessestonations_query
    generateUnitAccess,       # accessestounits_query
    generateActions,           # actions_query
    generateArmies,             # armies_query
    generateEvents,           # events_query
    generatePermissionTypes,  # permissions_query
    generateGrantedPermissions,  # grantedpermissions_query
    generateResourcesLoc,     # locationresources_query
    generateMaintenanceCosts, # maintenancecosts_query
    generateModifiers,        # modifiers_query
    generateTrade,            # tradeagreements_query
    generateTradeOffer,       # offeredresources_query
    generateOwnerships,       # ownedresources_query
    generatePops,             # populations_query
    generateProductionCost,   # productioncosts_query
    generateProductionShare,  # productionshares_query
    generateRelatedEvents,    # relatedevents_query
    generateTroops,           # troops_query
    generateOrders,           # unitorders_query
    generateUsedResource,     # usedresources_query
    generateWantedResource    # wantedresources_query
]



for i in range(len(queryList)):
    data=functionsList[i]()
    query=queryList[i]

    print(str(i)+":  "+queryList[i]+ "  ")
    cursor.executemany(query, data)

    connection.commit()


cursor.close()
connection.close()