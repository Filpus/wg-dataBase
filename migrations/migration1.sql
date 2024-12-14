-- Begin transaction (optional, recommended)
BEGIN;

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
-- Step 4: Migrate UnitOrders into Troops
-- Create a "Recruit" army per nation that has UnitOrders
-- This assumes fk_Nations in UnitOrders references a valid nation.
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

TRUNCATE TABLE UnitOrders;

-- After migration, remove UnitOrders if desired
TRUNCATE TABLE UnitOrders;

--------------------------------------------
-- Step 5: Remove volunteers from SocialGroups
--------------------------------------------
ALTER TABLE SocialGroups
  DROP COLUMN volunteers;

--------------------------------------------
-- Step 6: Remove volunteersNeeded from UnitTypes
--------------------------------------------
ALTER TABLE UnitTypes
  DROP COLUMN volunteersNeeded;

--------------------------------------------
-- Step 7: Remove quantity from Troops
--------------------------------------------
ALTER TABLE Troops
  DROP COLUMN quantity;

-- Commit transaction (if using transactions)
COMMIT;