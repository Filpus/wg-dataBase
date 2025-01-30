from neomodel import db

#ok
users_of_nations_query = """ 
MATCH (u:User)-[r:HASACCESTO]->(n:Nation)
WHERE u.isArchived = false AND r.isActive = true
RETURN n.name AS nation, COLLECT(u.name) AS active_players
ORDER BY n.name
"""


unresolved_actions_of_nation ="""
MATCH (n:Nation)<-[:PERFORMEDBY]-(a:Action)
WHERE n.name = $nation_name AND a.isSettled = false
RETURN a.name AS Action, a.description AS Description
ORDER BY a.name
"""


all_nation_resource_modifiers="""
MATCH (n:Nation)-[:TAKESPART]->(e:Event)-[:MODIFIESBYNUM]->(r:Resource)
WHERE n.name = $nation_name
RETURN r.name AS Resource, collect(e.name) AS Events, collect(r.value) AS Modifiers, 'Numeric' AS ModifierType

UNION

MATCH (n:Nation)-[:TAKESPART]->(e:Event)-[:MODIFIESBYPERC]->(r:Resource)
WHERE n.name = $nation_name
RETURN r.name AS Resource, collect(e.name) AS Events, collect(r.value) AS Modifiers, 'Percent' AS ModifierType

"""
whole_maintenance_cost_for_nation="""MATCH (n:Nation {name: $nation_name})<-[:BELONGSTO]-(a:Army)-[:AVAILABLETROOPS]->(u:UnitType)-[c:COSTTOMAINTAIN]->(r:Resource)
RETURN r.name AS ResourceName ,SUM(c.quantity) AS TotalSalary"""


# Query 1: The amount of each resource a nation has
resources_of_nation = """
MATCH (n:Nation {name: 'Spain'})-[r:OWNING]->(res:Resource)
RETURN n.name AS nation_name, res.name AS resource_name, r.amount AS resource_amount
"""

# Query 5: Pops number of a country
pops_of_country =""" 
MATCH (n:Nation)<-[:PLACEIN]-(loc:Localisation)<-[:RESIDES]-(pop:Pop)
RETURN n.name, COUNT(pop)"""

# Query 7: Number of volunteers in a country
volunteers_of_country = """
MATCH (n:Nation)<-[:PLACEIN]-(loc:Localisation)<-[:RESIDES]-(pop:Pop)-[:ISPARTOF]->(sg:SocialGroup)
RETURN n.name, SUM(sg.volunteers)"""

# Query 10: Localization of armies within a country
armies_localization_in_country ="""
MATCH (n:Nation)<-[:BELONGSTO]-(army:Army)-[:STAYINGAT]->(loc:Localisation)
RETURN n.name, army.name, loc.name"""