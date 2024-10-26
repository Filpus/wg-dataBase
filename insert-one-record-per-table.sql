-- Insert one record per table

INSERT INTO Cultures (name) VALUES ('Western');

INSERT INTO Religions (name) VALUES ('Christianity');

INSERT INTO SocialGroups (name, baseSatisfaction, volunteers) VALUES ('Workers', 0.7, 600);

INSERT INTO Locations (name, "size", fortifications, fk_Populations) VALUES ('Capital City', 100, 10, NULL);

INSERT INTO Populations (fk_SocialGroups, fk_Cultures, fk_Religions, fk_Locations, satisfaction) VALUES (1, 1, 1, 1, 0.8);

INSERT INTO Resources (name, isMain) VALUES ('Iron', TRUE);

INSERT INTO LocationResources (fk_Locations, fk_Resources, amount) VALUES (1, 1, 500);

INSERT INTO Nations (name, fk_Cultures, fk_Religions) VALUES ('Nation A', 1, 1);

INSERT INTO Armies (name, fk_Nations, fk_Locations) VALUES ('First Army', 1, 1);

INSERT INTO UnitTypes (name, melee, range, speed, morale, volunteersNeeded, isNaval) VALUES ('Infantry', 10, 0, 5, 7, 100, FALSE);

INSERT INTO Troops (quantity, fk_Armies, fk_UnitTypes) VALUES (50, 1, 1);

INSERT INTO ProductionCosts (fk_UnitTypes, fk_Resources, amount) VALUES (1, 1, 100);

INSERT INTO OwnedResources (fk_Nations, fk_Resources, amount) VALUES (1, 1, 300);

INSERT INTO TradeAgreements (fk_NationOffering, fk_NationReceiving, isAccepted) VALUES (1, 1, TRUE);

INSERT INTO Events (name, description) VALUES ('Harvest Festival', 'A celebration of the annual harvest.');

INSERT INTO Modifiers (fk_Events, target, fk_Resources, fk_SocialGroups, fk_Cultures, fk_Religions) VALUES (1, 'Zadowolenie', 1, 1, 1, 1);

INSERT INTO Users (name, email, password, isArchived) VALUES ('John Doe', 'john@example.com', 'password123', FALSE);

INSERT INTO AccessesToNations (fk_Nations, fk_Users, dateAcquired, isActive) VALUES (1, 1, '2024-01-01', TRUE);

INSERT INTO Permissions (name) VALUES ('Admin Access');

INSERT INTO GrantedPermissions (fk_Users, fk_Permissions) VALUES (1, 1);

INSERT INTO Actions (fk_Nations, name, description, result, isSettled) VALUES (1, 'Declare War', 'Declare war on neighboring country.', 'War declared successfully.', FALSE);

INSERT INTO UnitOrders (fk_Nations, fk_UnitTypes, quantity) VALUES (1, 1, 10);

INSERT INTO AccessesToUnits (fk_Nations, fk_UnitTypes) VALUES (1, 1);

INSERT INTO OfferedResources (fk_Resources, fk_TradeAgreements, amount) VALUES (1, 1, 200);

INSERT INTO WantedResources (fk_Resources, fk_TradeAgreements, amount) VALUES (1, 1, 150);

INSERT INTO RelatedEvents (fk_Nations, fk_Events) VALUES (1, 1);

INSERT INTO UsedResources (fk_SocialGroups, fk_Resources, amount) VALUES (1, 1, 50);

INSERT INTO ProductionShares (fk_SocialGroups, fk_Resources, coefficient) VALUES (1, 1, 0.5);

INSERT INTO MaintenanceCosts (fk_UnitTypes, fk_Resources, amount) VALUES (1, 1, 20);
-- Update Locations to set fk_Populations after Population is created
UPDATE Locations SET fk_Populations = 1 WHERE id = 1;