-- Begin transaction
BEGIN;

-- Step 0: Synchronize sequences after initial seeding
-- Adjust sequence names if needed
SELECT setval('armies_id_seq', (SELECT COALESCE(MAX(id), 0) FROM Armies) + 1);
SELECT setval('troops_id_seq', (SELECT COALESCE(MAX(id), 0) FROM Troops) + 1);

--------------------------------------------
-- Step 1: Add fk_religions to Armies
--------------------------------------------
ALTER TABLE Armies 
  ADD COLUMN fk_Religions INT4 NULL;

ALTER TABLE Armies
  ADD CONSTRAINT armies_fk_religions_fkey
    FOREIGN KEY (fk_Religions) REFERENCES Religions(id)
    ON DELETE SET NULL;

--------------------------------------------
-- Step 2: Add fk_populations to Troops
--------------------------------------------
ALTER TABLE Troops 
  ADD COLUMN fk_Populations INT4 NULL;

ALTER TABLE Troops
  ADD CONSTRAINT troops_fk_populations_fkey
    FOREIGN KEY (fk_Populations) REFERENCES Populations(id)
    ON DELETE SET NULL;

--------------------------------------------
-- Step 3: Add isRecruited to Troops
--------------------------------------------
ALTER TABLE Troops
  ADD COLUMN isRecruited BOOLEAN NOT NULL DEFAULT FALSE;

--------------------------------------------
-- Step 4: Remove quantity from Troops before inserting new rows
--------------------------------------------
ALTER TABLE Troops
  DROP COLUMN quantity;

--------------------------------------------
-- Step 5: Migrate UnitOrders into Troops
-- Create a "Recruit" army per nation that has UnitOrders
--------------------------------------------
WITH distinct_nations AS (
  SELECT DISTINCT fk_Nations 
  FROM UnitOrders
)
INSERT INTO Armies (name, fk_Nations, fk_Locations, fk_Religions)
SELECT 'Recruit', dn.fk_Nations, l.id, NULL
FROM distinct_nations dn
JOIN LATERAL (
  SELECT id 
  FROM Locations 
  WHERE fk_Nations = dn.fk_Nations
  ORDER BY id
  LIMIT 1
) l ON true;

WITH recruit_armies AS (
  SELECT a.id AS army_id, a.fk_Nations
  FROM Armies a
  WHERE a.name = 'Recruit'
)
INSERT INTO Troops (fk_Armies, fk_UnitTypes, isRecruited)
SELECT ra.army_id, uo.fk_UnitTypes, FALSE
FROM UnitOrders uo
JOIN recruit_armies ra ON ra.fk_Nations = uo.fk_Nations
JOIN generate_series(1, uo.quantity) gs ON TRUE;

-- Clear UnitOrders since they are now fulfilled
TRUNCATE TABLE UnitOrders;

--------------------------------------------
-- Step 6: Assign populations to troops
-- We match troops and populations by nation using a row number pairing:
--   - Sort troops by nation, then by troop ID
--   - Sort populations by nation, then by population ID
--   - Assign the first population in a nation to the first troop in that nation, the second to the second, etc.
-- If there aren't enough populations for all troops, the unmatched troops remain NULL.
--------------------------------------------
WITH sorted_troops AS (
    SELECT tr.id AS troop_id,
           a.fk_Nations,
           ROW_NUMBER() OVER(PARTITION BY a.fk_Nations ORDER BY tr.id) AS t_rn
    FROM Troops tr
    JOIN Armies a ON tr.fk_Armies = a.id
),
sorted_pops AS (
    SELECT p.id AS pop_id,
           loc.fk_Nations AS fk_Nations,
           ROW_NUMBER() OVER(PARTITION BY loc.fk_Nations ORDER BY p.id) AS p_rn
    FROM Populations p
    JOIN Locations loc ON p.fk_Locations = loc.id
)
UPDATE Troops tr
SET fk_Populations = sp.pop_id
FROM sorted_troops st
JOIN sorted_pops sp
  ON st.fk_Nations = sp.fk_Nations
 AND st.t_rn = sp.p_rn
WHERE tr.id = st.troop_id;

--------------------------------------------
-- Step 7: Remove volunteers from SocialGroups
--------------------------------------------
ALTER TABLE SocialGroups
  DROP COLUMN volunteers;

--------------------------------------------
-- Step 8: Remove volunteersNeeded from UnitTypes
--------------------------------------------
ALTER TABLE UnitTypes
  DROP COLUMN volunteersNeeded;

-- Commit transaction
COMMIT;
