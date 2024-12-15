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
    nation.name = 'Spain';

-- Query 2: Country assigned to each player
SELECT
    nations.name AS nation_name,
    users.name AS username
FROM
    accessestonations access
JOIN
    users ON access.fk_users =users.id
JOIN
    nations ON access.fk_nations = nations.id
;


-- Query 3: Average happiness of the population in a given country by culture
SELECT c.name AS culture_name, ROUND(AVG(p.happiness)::numeric, 2) AS average_happiness
FROM Populations p
JOIN Cultures c ON p.fk_Cultures = c.id
JOIN Locations l ON p.fk_Locations = l.id
JOIN Nations n ON l.fk_Nations = n.id  -- Replace 'Ukraine' with the country name
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

-- Query 6:  Total pay for soldiers in the nation per turn (parameter: nation)
SELECT
    r.name AS nazwa_zasobu,
    SUM(mc.amount * t.quantity) AS sumaryczna_ilosc
FROM
    Troops t
JOIN
    Armies a ON t.fk_Armies = a.id
JOIN
    Nations n ON a.fk_Nations = n.id
JOIN
    MaintenanceCosts mc ON t.fk_UnitTypes = mc.fk_UnitTypes
JOIN
    Resources r ON mc.fk_Resources = r.id
WHERE
    n.name = :nazwa_panstwa
GROUP BY
    r.name
ORDER BY
    nazwa_zasobu;


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
    nation.name = '';

-- Query 11: List of unresolved actions of a nation (parameter: nation)
SELECT
    a.name AS nazwa_akcji,
    a.description AS opis_akcji,
    a.isSettled AS czy_rozpatrzona
FROM
    Actions a
JOIN
    Nations n ON a.fk_Nations = n.id
WHERE
    n.name = :nazwa_panstwa
    AND a.isSettled = FALSE
ORDER BY
    a.name;

-- Query 12: Number of followers of a given religion in the game
SELECT r.name AS religion_name,
COUNT(p.id) AS total_followers
FROM Religions r
LEFT JOIN Populations p ON p.fk_Religions = r.id
GROUP BY r.name
ORDER BY total_followers DESC, r.name ASC;

--Query 14: All production modifiers of a resource of a nation (parameters: resource, nation)
    SELECT
    m.id AS id_modyfikatora,
    m.target AS cel_modyfikatora,
    e.name AS nazwa_wydarzenia,
    e.description AS opis_wydarzenia,
    r.name AS nazwa_zasobu,
    sg.name AS grupa_spoleczna
FROM
    Modifiers m
JOIN
    Events e ON m.fk_Events = e.id
JOIN
    Resources r ON m.fk_Resources = r.id
LEFT JOIN
    SocialGroups sg ON m.fk_SocialGroups = sg.id
JOIN
    Nations n ON n.fk_Cultures = sg.id OR n.fk_Religions = sg.id
WHERE
    n.name = :nazwa_panstwa
    AND r.name = :nazwa_zasobu
    AND m.target = 'Production'
ORDER BY
    m.id;


-- Query 16: Displaying nations that have more than 'X' of a given resource 'Y'
SELECT n.name AS nation_name, r.name AS resource_name, owned_res.amount AS resource_amount
FROM Nations n
JOIN OwnedResources owned_res ON n.id = owned_res.fk_Nations
JOIN Resources r ON owned_res.fk_Resources = r.id
WHERE r.name = 'data'  -- Replace 'year' with the resource name
AND owned_res.amount > 800  -- Replace '100' with the minimum amount of resource
ORDER BY owned_res.amount DESC, n.name ASC;