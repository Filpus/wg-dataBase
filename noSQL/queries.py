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

### BEGIN RYCHU QUERIES ###

average_satisfaction="""
MATCH (n:Nation {name: $nationName})<-[:PLACEIN]-(l:Localisation)<-[:RESIDES]-(p:Pop)-[:CULTIVATES]->(c:Culture)
WITH c.name AS culture_name, AVG(p.satisfaction) AS avg_satisfaction
RETURN culture_name, ROUND(avg_satisfaction * 100) / 100 AS average_satisfaction
ORDER BY average_satisfaction DESC;
"""
who_trades_with_whom="""
MATCH (n1:Nation)<-[:ISOFFERING]-(ta:TradeAgreement {isAccepted: true})-[:ISRECEIVING]->(n2:Nation)
RETURN DISTINCT n1.name AS nation_offering, n2.name AS nation_receiving
ORDER BY nation_offering ASC, nation_receiving ASC;
"""
number_of_followers_by_religion="""
MATCH (r:Religion)
OPTIONAL MATCH (p:Pop)-[:WORSHIP]->(r)
WITH r.name AS religion_name, COUNT(p) AS total_followers
RETURN religion_name, total_followers
ORDER BY total_followers DESC, religion_name ASC;

"""
nations_with_more_than_x_of_resource_y="""
MATCH (n:Nation)-[o:OWNING]->(r:Resource {name: $resourceName})
WHERE o.amount > $minAmount
RETURN n.name AS nation_name, r.name AS resource_name, o.amount AS resource_amount
ORDER BY resource_amount DESC, nation_name ASC;

"""
### END RYCHU QUERIES ###

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
