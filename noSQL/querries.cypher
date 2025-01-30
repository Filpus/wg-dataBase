MATCH (n:Nation {name: 'Spain'})-[r:OWNING]->(res:Resource)
RETURN n.name AS nation_name, res.name AS resource_name, r.amount AS resource_amount

MATCH (n:Nation)<-[:BELONGS_TO]-(loc:Localisation)<-[:RESIDES]-(pop:Pop)
RETURN n.name AS nation_name, COUNT(pop) AS pop_count