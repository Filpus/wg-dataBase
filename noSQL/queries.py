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
MATCH (n:Nation)-[:HAPPENSIN]->(e:Event)-[:MODIFIESBYNUM]->(r:Resource)
WHERE n.name = $nation_name
RETURN r.name AS Resource, collect(e.name) AS Events, collect(r.value) AS NumericModifiers

UNION

MATCH (n:Nation)-[:HAPPENSIN]->(e:Event)-[:MODIFIESBYPERC]->(r:Resource)
WHERE n.name = $nation_name
RETURN r.name AS Resource, collect(e.name) AS Events, collect(r.value) AS PercentModifiers
"""