CREATE OR REPLACE FUNCTION avg_happiness_by_nation(nation_id INT)
    RETURNS TABLE(location_id INT, location_name VARCHAR, average_happiness FLOAT) AS $$
BEGIN
    RETURN QUERY
        SELECT
            l.id,
            l.name,
            AVG(p.happiness)
        FROM
            Locations l
                JOIN
            Nations n ON l.fk_Nations = n.id
                JOIN
            Populations p ON p.fk_Locations = l.id
        WHERE
            n.id = nation_id
        GROUP BY
            l.id, l.name;
END;
$$ LANGUAGE plpgsql;

EXPLAIN SELECT * FROM avg_happiness_by_nation(1); -- gdzie 1 to id państwa

EXPLAIN ANALYSE  SELECT
    n.id AS nation_id,
    n.name AS nation_name,
    COUNT(t) AS total_army_size
FROM
    Nations n
        JOIN
    Armies a ON a.fk_Nations = n.id
        JOIN
    Troops t ON t.fk_Armies = a.id
GROUP BY
    n.id, n.name
ORDER BY
    total_army_size DESC;

CREATE OR REPLACE FUNCTION get_population_by_religion_culture_social_group(nation_id INT)
    RETURNS TABLE (
                      religion_name VARCHAR,
                      culture_name VARCHAR,
                      social_group_name VARCHAR,
                      population_count BIGINT
                  ) AS $$
BEGIN
    RETURN QUERY
        SELECT
            r.name AS religion_name,
            c.name AS culture_name,
            sg.name AS social_group_name,
            COUNT(p.id) AS population_count
        FROM
            Populations p
                JOIN
            Religions r ON p.fk_Religions = r.id
                JOIN
            Cultures c ON p.fk_Cultures = c.id
                JOIN
            SocialGroups sg ON p.fk_SocialGroups = sg.id
                JOIN
            Locations l ON p.fk_Locations = l.id
                JOIN
            Nations n ON l.fk_Nations = n.id
        WHERE
            n.id = nation_id  -- filtruj według identyfikatora państwa
        GROUP BY
            r.name, c.name, sg.name
        ORDER BY
            population_count DESC;
END;
$$ LANGUAGE plpgsql;


EXPLAIN ANALYSE select
    nations.name as nation,
    nations.id as id,
    resources.name as recource,
    sum(maintenancecosts.amount) as maintanceCost
FROM
    nations
        left join armies on nations.id = armies.fk_nations
        left join troops on armies.id = troops.fk_armies
        left join unittypes on troops.fk_unittypes = unittypes.id
        left join maintenancecosts on unittypes.id = maintenancecosts.fk_unittypes
        left join resources on maintenancecosts.fk_resources = resources.id
WHERE
    nations.id = 1
GROUP BY
    nations.id, resources.id
;

EXPLAIN ANALYSE SELECT

    nations.name as nation,
    nations.id as id,
    resources.name as recource,
    sum(usedresources.amount) as usedresources
FROM
    nations
        left join locations on nations.id = locations.fk_nations
        left join populations on locations.id = populations.fk_locations
        left join socialgroups on populations.fk_socialgroups = socialgroups.id
        left join  usedresources on socialgroups.id = usedresources.fk_socialgroups
        left join resources on usedresources.fk_resources = resources.id
GROUP BY
    nations.name, nations.id, resources.name;