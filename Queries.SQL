-- Query 1: The amount of each resource a nation has
SELECT 
    nation.name AS nation_name,
    resource.name AS resource_name,
    owned_resources.amount AS resource_amount
FROM 
    Nations nation
JOIN 
    OwnedResources owned_resources ON nation.id = owned_resources.fk_Nations
JOIN 
    Resources resource ON owned_resources.fk_Resources = resource.id
WHERE 
    nation.name = 'Poland';

-- Query 3: Average happiness of the population in a given country by culture
SELECT c.name AS culture_name, ROUND(AVG(p.happiness)::numeric, 2) AS average_happiness
FROM Populations p
JOIN Cultures c ON p.fk_Cultures = c.id
JOIN Locations l ON p.fk_Locations = l.id
JOIN Nations n ON l.fk_Nations = n.id
WHERE n.name = 'Ukraine'  -- Replace 'Ukraine' with the country name
GROUP BY c.name
ORDER BY average_happiness DESC;

-- Query 5: Pops number of a country
SELECT 
    nation.name AS nation_name,
    COUNT(pop.id) AS pop_count
FROM
    Nations nation
JOIN
    Locations loc ON nation.id = loc.fk_Nations
JOIN
    Populations pop ON loc.id = pop.fk_Locations
GROUP BY 
    nation.name;

-- Query 7: Number of volunteers in a country
SELECT 
    nation.name AS nation_name,
    SUM(sg.volunteers) AS total_volunteers
FROM
    Nations nation
JOIN 
    Locations loc ON nation.id = loc.fk_Nations
JOIN 
    Populations pop ON loc.id = pop.fk_Locations
JOIN 
    SocialGroups sg ON pop.fk_SocialGroups = sg.id
WHERE
    nation.name = 'Specific Nation Name'
GROUP BY 
    nation.name;

-- Query 8: List of who is trading with whom
SELECT DISTINCT n1.name AS nation_offering, n2.name AS nation_receiving
FROM TradeAgreements ta
JOIN Nations n1 ON ta.fk_NationOffering = n1.id
JOIN Nations n2 ON ta.fk_NationReceiving = n2.id
WHERE ta.isAccepted
ORDER BY n1.name ASC, n2.name ASC;

-- Query 10: Localization of armies within a country
SELECT 
    nation.name AS nation_name,
    army.name AS army_name,
    loc.name AS location_name
FROM
    Armies army
JOIN 
    Locations loc ON army.fk_Locations = loc.id
JOIN 
    Nations nation ON loc.fk_Nations = nation.id
WHERE 
    nation.name = 'Poland';

-- Query 12: Number of followers of a given religion in the game
SELECT r.name AS religion_name,
COUNT(p.id) AS total_followers
FROM Religions r
LEFT JOIN Populations p ON p.fk_Religions = r.id
GROUP BY r.name
ORDER BY total_followers DESC, r.name ASC;

-- Query 16: Displaying nations that have more than 'X' of a given resource 'Y'
SELECT n.name AS nation_name, r.name AS resource_name, owned_res.amount AS resource_amount
FROM Nations n
JOIN OwnedResources owned_res ON n.id = owned_res.fk_Nations
JOIN Resources r ON owned_res.fk_Resources = r.id
WHERE r.name = 'year'  -- Replace 'year' with the resource name
AND owned_res.amount > 100  -- Replace '100' with the minimum amount of resource
ORDER BY owned_res.amount DESC, n.name ASC;