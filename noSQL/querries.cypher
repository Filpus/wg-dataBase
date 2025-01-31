//Query 1: The amount of each resource a nation has
MATCH (n:Nation {name: 'Spain'})-[r:OWNING]->(res:Resource)
RETURN n.name AS nation_name, res.name AS resource_name, r.amount AS resource_amount

//Query 5: Pops number of a country
MATCH (n:Nation)<-[:BELONGSTO]-(loc:Localisation)<-[:RESIDES]-(pop:Pop)
RETURN n.name AS nation_name, COUNT(pop) AS pop_count

//Query 7: Number of volunteers in a country
MATCH (n:Nation)<-[:BELONGSTO]-(loc:Localisation)<-[:RESIDES]-(pop:Pop)-[:ISPARTOF]->(sg:SocialGroup)
RETURN n.name AS nation_name, SUM(sg.volunteers) AS total_volunteers

//Query 10: Localization of armies within a country
MATCH (n:Nation)<-[:BELONGSTO]-(loc:Localisation)<-[:STAYINGAT]-(army:Army)
RETURN n.name AS nation_name, army.name AS army_name, loc.name AS location_name