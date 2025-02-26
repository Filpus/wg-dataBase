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
cultures_query = '''INSERT INTO cultures (name) VALUES (%s);'''
religions_query = '''INSERT INTO religions (name) VALUES (%s);'''
resources_query = '''INSERT INTO resources ( name, ismain) VALUES ( %s,%s);'''
socialgroups_query = '''INSERT INTO socialgroups ( name, baseHappiness, volunteers) VALUES ( %s,%s, %s);'''
users_query = '''INSERT INTO users ( name,email,password,isarchived) VALUES ( %s,%s, %s,%s);'''
unittypes_query = '''INSERT INTO unittypes ( name,melee, range,defense,speed,morale,volunteersneeded,isnaval) VALUES ( %s,%s,%s, %s,%s, %s,%s, %s);'''

# Encje zależne
nations_query = '''INSERT INTO nations ( name,fk_cultures,fk_religions) VALUES ( %s,%s, %s);'''
locations_query = '''INSERT INTO locations ( name,size,fortifications,fk_nations) VALUES ( %s,%s, %s,%s);'''
accessestonations_query = '''INSERT INTO accessestonations ( fk_nations,fk_users,dateacquired,isactive) VALUES ( %s,%s, %s,%s);'''
accessestounits_query = '''INSERT INTO accessestounits (fk_nations, fk_unittypes ) VALUES ( %s,%s);'''
actions_query = '''INSERT INTO actions (fk_nations,name,description,result,issettled) VALUES ( %s,%s,%s, %s,%s);'''
armies_query = '''INSERT INTO armies ( name, fk_nations, fk_locations) VALUES ( %s,%s, %s);'''
events_query = '''INSERT INTO events ( name,description) VALUES ( %s, %s);'''
grantedpermissions_query = '''INSERT INTO grantedpermissions ( fk_users, fk_permissions) VALUES ( %s,%s);'''
locationresources_query = '''INSERT INTO locationresources ( fk_locations, fk_resources,amount) VALUES ( %s,%s, %s);'''
maintenancecosts_query = '''INSERT INTO maintenancecosts ( fk_unittypes,fk_resources,amount) VALUES ( %s,%s, %s);'''
modifiers_query = '''INSERT INTO modifiers ( fk_events,target,fk_resources,fk_socialgroups,fk_cultures,fk_religions) VALUES ( %s,%s, %s,%s, %s,%s);'''
offeredresources_query = '''INSERT INTO offeredresources ( fk_resources,fk_tradeagreements, amount) VALUES ( %s,%s, %s);'''
ownedresources_query = '''INSERT INTO ownedresources ( fk_nations, fk_resources,amount) VALUES ( %s,%s, %s);'''
permissions_query = '''INSERT INTO permissions ( name) VALUES ( %s);'''
populations_query = '''INSERT INTO populations (fk_socialgroups, fk_cultures, fk_religions, fk_locations, happiness) VALUES ( %s,%s, %s,%s, %s);'''
productioncosts_query = '''INSERT INTO productioncosts ( fk_unittypes, fk_resources, amount) VALUES ( %s,%s, %s);'''
productionshares_query = '''INSERT INTO productionshares ( fk_socialgroups, fk_resources, coefficient) VALUES ( %s,%s, %s);'''
relatedevents_query = '''INSERT INTO relatedevents ( fk_nations, fk_events) VALUES (%s,%s);'''
tradeagreements_query = '''INSERT INTO tradeagreements ( fk_nationoffering, fk_nationreceiving,isaccepted,duration) VALUES ( %s,%s, %s,%s);'''
troops_query = '''INSERT INTO troops ( quantity, fk_armies, fk_unittypes) VALUES ( %s,%s, %s);'''
unitorders_query = '''INSERT INTO unitorders ( fk_nations, fk_unittypes, quantity) VALUES ( %s,%s, %s);'''
usedresources_query = '''INSERT INTO usedresources  ( fk_socialgroups,fk_resources,amount) VALUES ( %s,%s, %s);'''
wantedresources_query = '''INSERT INTO wantedresources ( fk_resources,fk_tradeagreements,amount) VALUES ( %s,%s, %s);'''



queryList= [
    ##cultures_query,
    ##religions_query,
    ## nations_query,
    ## resources_query,
    ## locations_query,
    ## socialgroups_query,
    ## users_query,
    # unittypes_query,
    ## accessestonations_query,
    # accessestounits_query,
    # actions_query,
    # armies_query,
    # events_query,
    # permissions_query,
    # grantedpermissions_query,
    # locationresources_query,
    # maintenancecosts_query,
    # modifiers_query,
    # tradeagreements_query,
    # offeredresources_query,
    ##ownedresources_query,
     populations_query,
    # productioncosts_query,
    # productionshares_query,
    # relatedevents_query,
    # troops_query,
    # unitorders_query,
    # usedresources_query,
    # wantedresources_query
]

functionsList = [
    ##generateCulture,          # cultures_query
    ##generateReligions,        # religion_query
    ##generateNations,          # nations_query
    ##generateResources,        # resources_query
    ##generateLocations,        # locations_query
    ##generateSocialGroups,      # socialgroups_query
    ##generateUsers,            # users_query
    # generateUnitTypes,        # unittypes_query
    ##generateNationAccess,     # accessestonations_query
    # generateUnitAccess,       # accessestounits_query
    # generateActions,           # actions_query
    # generateArmies,             # armies_query
    # generateEvents,           # events_query
    # generatePermissionTypes,  # permissions_query
    # generateGrantedPermissions,  # grantedpermissions_query
    # generateResourcesLoc,     # locationresources_query
    # generateMaintenanceCosts, # maintenancecosts_query
    # generateModifiers,        # modifiers_query
    # generateTrade,            # tradeagreements_query
    # generateTradeOffer,       # offeredresources_query
    ##generateOwnerships,       # ownedresources_query
     generatePops,             # populations_query
    # generateProductionCost,   # productioncosts_query
    # generateProductionShare,  # productionshares_query
    # generateRelatedEvents,    # relatedevents_query
    # generateTroops,           # troops_query
    # generateOrders,           # unitorders_query
    # generateUsedResource,     # usedresources_query
    # generateWantedResource    # wantedresources_query
]

for i in range(len(queryList)):
    print(str(i)+" executing :  "+functionsList[i].__name__+ "  ")
    data=functionsList[i]()
    query=queryList[i]

    print(str(i)+" writing:  "+queryList[i]+ "  ")
    cursor.executemany(query, data)

    connection.commit()


cursor.close()
connection.close()