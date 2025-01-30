from neomodel import db

users_of_nations_query = """
MATCH (u:User)-[r:HASACCESTO]->(n:Nation)
WHERE u.isArchived = false AND r.isActive = true
RETURN n.name AS nation, COLLECT(u.name) AS active_players
ORDER BY n.name
"""



results, _ = db.cypher_query(users_of_nations_query)
