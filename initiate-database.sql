-- Enum definitions
CREATE TYPE target_enum AS ENUM ('Happiness', 'Production');

-- Table definitions
CREATE TABLE Cultures (id SERIAL NOT NULL, name VARCHAR(255) NOT NULL UNIQUE, PRIMARY KEY (id));

CREATE TABLE Religions (id SERIAL NOT NULL, name VARCHAR(255) NOT NULL UNIQUE, PRIMARY KEY (id));

CREATE TABLE SocialGroups (id SERIAL NOT NULL, name VARCHAR(255) NOT NULL UNIQUE, baseSatisfaction float4 DEFAULT 0.5 NOT NULL, volunteers int4 DEFAULT 500 NOT NULL, PRIMARY KEY (id));
ALTER TABLE SocialGroups 
ADD CONSTRAINT base_satisfaction_check CHECK (baseSatisfaction >= 0 AND baseSatisfaction <= 1),
ADD CONSTRAINT volunteers_check CHECK (volunteers >= 0);

CREATE TABLE Populations (id SERIAL NOT NULL, fk_SocialGroups int4 NOT NULL, fk_Cultures int4 NOT NULL, fk_Religions int4 NOT NULL, fk_Locations int4 NOT NULL, satisfaction float4 NOT NULL, PRIMARY KEY (id));
ALTER TABLE Populations 
ADD CONSTRAINT satisfaction_check CHECK (satisfaction >= 0 AND satisfaction <= 1);

CREATE TABLE Locations (id SERIAL NOT NULL, name VARCHAR(255) NOT NULL UNIQUE, "size" int4 NOT NULL, fortifications int4 DEFAULT 0 NOT NULL, fk_Nations int4 NOT NULL, PRIMARY KEY (id));
ALTER TABLE Locations 
ADD CONSTRAINT size_check CHECK ("size" > 0),
ADD CONSTRAINT fortifications_check CHECK (fortifications >= 0);

CREATE TABLE LocationResources (id SERIAL NOT NULL, fk_Locations int4 NOT NULL, fk_Resources int4 NOT NULL, amount int4 NOT NULL, PRIMARY KEY (id));
ALTER TABLE LocationResources
ADD CONSTRAINT location_resources_amount_check CHECK (amount >= 0);

CREATE TABLE Resources (id SERIAL NOT NULL, name VARCHAR(255) NOT NULL UNIQUE, isMain BOOLEAN DEFAULT FALSE NOT NULL, PRIMARY KEY (id));

CREATE TABLE Armies (id SERIAL NOT NULL, name VARCHAR(255) NOT NULL, fk_Nations int4 NOT NULL, fk_Locations int4 NOT NULL, PRIMARY KEY (id));

CREATE TABLE Troops (id SERIAL NOT NULL, quantity int4 NOT NULL, fk_Armies int4 NOT NULL, fk_UnitTypes int4 NOT NULL, PRIMARY KEY (id));
ALTER TABLE Troops 
ADD CONSTRAINT quantity_check CHECK (quantity > 0);

CREATE TABLE UnitTypes (id SERIAL NOT NULL, name VARCHAR(255) NOT NULL UNIQUE, melee int4 NOT NULL, range int4 DEFAULT 0 NOT NULL, speed int4 NOT NULL, morale int4 NOT NULL, volunteersNeeded int4 NOT NULL, isNaval BOOLEAN NOT NULL, PRIMARY KEY (id));

CREATE TABLE Nations (id SERIAL NOT NULL, name VARCHAR(255) NOT NULL UNIQUE, fk_Cultures int4 NOT NULL, fk_Religions int4 NOT NULL, PRIMARY KEY (id));

CREATE TABLE ProductionCosts (id SERIAL NOT NULL, fk_UnitTypes int4 NOT NULL, fk_Resources int4 NOT NULL, amount int4, PRIMARY KEY (id));
ALTER TABLE ProductionCosts
ADD CONSTRAINT amount_check CHECK (amount >= 0);

CREATE TABLE OwnedResources (id SERIAL NOT NULL, fk_Nations int4 NOT NULL, fk_Resources int4 NOT NULL, amount int4 NOT NULL, PRIMARY KEY (id));
ALTER TABLE OwnedResources
ADD CONSTRAINT owned_resources_amount_check CHECK (amount >= 0);

CREATE TABLE TradeAgreements (id SERIAL NOT NULL, fk_NationOffering int4 NOT NULL, fk_NationReceiving int4 NOT NULL, isAccepted BOOLEAN NOT NULL, PRIMARY KEY (id));

CREATE TABLE Events (id SERIAL NOT NULL, name VARCHAR(255) NOT NULL, description VARCHAR(255), PRIMARY KEY (id));

CREATE TABLE Modifiers (id SERIAL NOT NULL, fk_Events int4 NOT NULL, target VARCHAR(255) NOT NULL, fk_Resources int4, fk_SocialGroups int4, fk_Cultures int4, fk_Religions int4, PRIMARY KEY (id));
ALTER TABLE Modifiers
ALTER COLUMN target TYPE target_enum USING target::target_enum;

CREATE TABLE Users (id SERIAL NOT NULL, name VARCHAR(255) NOT NULL UNIQUE, email VARCHAR(255) NOT NULL UNIQUE, password VARCHAR(255) NOT NULL, isArchived BOOLEAN NOT NULL, PRIMARY KEY (id));

CREATE TABLE AccessesToNations (id SERIAL NOT NULL, fk_Nations int4 NOT NULL, fk_Users int4 NOT NULL, dateAcquired date, isActive BOOLEAN DEFAULT TRUE NOT NULL, PRIMARY KEY (id));

CREATE TABLE Permissions (id SERIAL NOT NULL, name VARCHAR(255) NOT NULL UNIQUE, PRIMARY KEY (id));

CREATE TABLE GrantedPermissions (id SERIAL NOT NULL, fk_Users int4 NOT NULL, fk_Permissions int4 NOT NULL, PRIMARY KEY (id));

CREATE TABLE Actions (id SERIAL NOT NULL, fk_Nations int4 NOT NULL, name VARCHAR(255), description VARCHAR(25000) NOT NULL, result VARCHAR(25000), isSettled BOOLEAN DEFAULT FALSE NOT NULL, PRIMARY KEY (id));

CREATE TABLE UnitOrders (id SERIAL NOT NULL, fk_Nations int4 NOT NULL, fk_UnitTypes int4 NOT NULL, quantity int4 DEFAULT 1 NOT NULL, PRIMARY KEY (id));
ALTER TABLE UnitOrders
ADD CONSTRAINT unit_orders_quantity_check CHECK (quantity >= 0);

CREATE TABLE AccessesToUnits (id SERIAL NOT NULL, fk_Nations int4 NOT NULL, fk_UnitTypes int4 NOT NULL, PRIMARY KEY (id));

CREATE TABLE OfferedResources (id SERIAL NOT NULL, fk_Resources int4 NOT NULL, fk_TradeAgreements int4 NOT NULL, amount int4 NOT NULL, PRIMARY KEY (id));
ALTER TABLE OfferedResources
ADD CONSTRAINT offered_resources_amount_check CHECK (amount >= 0);

CREATE TABLE WantedResources (id SERIAL NOT NULL, fk_Resources int4 NOT NULL, fk_TradeAgreements int4 NOT NULL, amount int4 NOT NULL, PRIMARY KEY (id));
ALTER TABLE WantedResources
ADD CONSTRAINT wanted_resources_amount_check CHECK (amount >= 0);

CREATE TABLE RelatedEvents (id SERIAL NOT NULL, fk_Nations int4 NOT NULL, fk_Events int4 NOT NULL, PRIMARY KEY (id));

CREATE TABLE UsedResources (id SERIAL NOT NULL, fk_SocialGroups int4 NOT NULL, fk_Resources int4 NOT NULL, amount int4 NOT NULL, PRIMARY KEY (id));
ALTER TABLE UsedResources
ADD CONSTRAINT used_resources_amount_check CHECK (amount >= 0);

CREATE TABLE ProductionShares (id SERIAL NOT NULL, fk_SocialGroups int4 NOT NULL, fk_Resources int4 NOT NULL, coefficient float4 NOT NULL, PRIMARY KEY (id));
ALTER TABLE ProductionShares
ADD CONSTRAINT coefficient_check CHECK (coefficient >= 0);

CREATE TABLE MaintenanceCosts (id SERIAL NOT NULL, fk_UnitTypes int4 NOT NULL, fk_Resources int4 NOT NULL, amount int4 NOT NULL, PRIMARY KEY (id));
ALTER TABLE MaintenanceCosts
ADD CONSTRAINT maintenance_costs_amount_check CHECK (amount >= 0);

-- Foreign keys
ALTER TABLE Populations 
ADD CONSTRAINT fk_population_socialgroups 
FOREIGN KEY (fk_SocialGroups) 
REFERENCES SocialGroups(id) 
ON DELETE SET NULL;

ALTER TABLE Populations
ADD CONSTRAINT fk_population_cultures
FOREIGN KEY (fk_Cultures)
REFERENCES Cultures(id)
ON DELETE SET NULL;

ALTER TABLE Populations
ADD CONSTRAINT fk_population_religions
FOREIGN KEY (fk_Religions)
REFERENCES Religions(id)
ON DELETE SET NULL;

ALTER TABLE Populations
ADD CONSTRAINT fk_population_locations
FOREIGN KEY (fk_Locations)
REFERENCES Locations(id)
ON DELETE SET NULL;

ALTER TABLE Locations
ADD CONSTRAINT fk_location_nations
FOREIGN KEY (fk_Nations)
REFERENCES Nations(id)
ON DELETE SET NULL;

ALTER TABLE LocationResources
ADD CONSTRAINT fk_locationresources_locations
FOREIGN KEY (fk_Locations)
REFERENCES Locations(id)
ON DELETE CASCADE;

ALTER TABLE LocationResources
ADD CONSTRAINT fk_locationresources_resources
FOREIGN KEY (fk_Resources)
REFERENCES Resources(id)
ON DELETE CASCADE;

ALTER TABLE Armies
ADD CONSTRAINT fk_armies_nations
FOREIGN KEY (fk_Nations)
REFERENCES Nations(id)
ON DELETE SET NULL;

ALTER TABLE Armies
ADD CONSTRAINT fk_armies_locations
FOREIGN KEY (fk_Locations)
REFERENCES Locations(id)
ON DELETE SET NULL;

ALTER TABLE Troops
ADD CONSTRAINT fk_troops_armies
FOREIGN KEY (fk_Armies)
REFERENCES Armies(id)
ON DELETE CASCADE;

ALTER TABLE Troops
ADD CONSTRAINT fk_troops_unitTypes
FOREIGN KEY (fk_UnitTypes)
REFERENCES UnitTypes(id)
ON DELETE CASCADE;

ALTER TABLE Nations
ADD CONSTRAINT fk_nations_cultures
FOREIGN KEY (fk_Cultures)
REFERENCES Cultures(id)
ON DELETE SET NULL;

ALTER TABLE Nations
ADD CONSTRAINT fk_nations_religions
FOREIGN KEY (fk_Religions)
REFERENCES Religions(id)
ON DELETE SET NULL;

ALTER TABLE ProductionCosts
ADD CONSTRAINT fk_productionCosts_unitTypes
FOREIGN KEY (fk_UnitTypes)
REFERENCES UnitTypes(id)
ON DELETE CASCADE;

ALTER TABLE ProductionCosts
ADD CONSTRAINT fk_productionCosts_resources
FOREIGN KEY (fk_Resources)
REFERENCES Resources(id)
ON DELETE CASCADE;

ALTER TABLE OwnedResources
ADD CONSTRAINT fk_ownedResources_nations
FOREIGN KEY (fk_Nations)
REFERENCES Nations(id)
ON DELETE SET NULL;

ALTER TABLE OwnedResources
ADD CONSTRAINT fk_ownedResources_resources
FOREIGN KEY (fk_Resources)
REFERENCES Resources(id)
ON DELETE CASCADE;

ALTER TABLE TradeAgreements
ADD CONSTRAINT fk_tradeAgreements_nationOffering
FOREIGN KEY (fk_NationOffering)
REFERENCES Nations(id)
ON DELETE SET NULL;

ALTER TABLE TradeAgreements
ADD CONSTRAINT fk_tradeAgreements_nationReceiving
FOREIGN KEY (fk_NationReceiving)
REFERENCES Nations(id)
ON DELETE SET NULL;

ALTER TABLE Modifiers
ADD CONSTRAINT fk_modifiers_events
FOREIGN KEY (fk_Events)
REFERENCES Events(id)
ON DELETE SET NULL;

ALTER TABLE Modifiers
ADD CONSTRAINT fk_modifiers_resources
FOREIGN KEY (fk_Resources)
REFERENCES Resources(id)
ON DELETE SET NULL;

ALTER TABLE Modifiers
ADD CONSTRAINT fk_modifiers_socialGroups
FOREIGN KEY (fk_SocialGroups)
REFERENCES SocialGroups(id)
ON DELETE SET NULL;

ALTER TABLE Modifiers
ADD CONSTRAINT fk_modifiers_cultures
FOREIGN KEY (fk_Cultures)
REFERENCES Cultures(id)
ON DELETE SET NULL;

ALTER TABLE Modifiers
ADD CONSTRAINT fk_modifiers_religions
FOREIGN KEY (fk_Religions)
REFERENCES Religions(id)
ON DELETE SET NULL;

ALTER TABLE AccessesToNations
ADD CONSTRAINT fk_accessesToNations_nations
FOREIGN KEY (fk_Nations)
REFERENCES Nations(id)
ON DELETE SET NULL;

ALTER TABLE AccessesToNations
ADD CONSTRAINT fk_accessesToNations_users
FOREIGN KEY (fk_Users)
REFERENCES Users(id)
ON DELETE CASCADE;

ALTER TABLE GrantedPermissions
ADD CONSTRAINT fk_grantedPermissions_users
FOREIGN KEY (fk_Users)
REFERENCES Users(id)
ON DELETE CASCADE;

ALTER TABLE GrantedPermissions
ADD CONSTRAINT fk_grantedPermissions_permissions
FOREIGN KEY (fk_Permissions)
REFERENCES Permissions(id)
ON DELETE CASCADE;

ALTER TABLE Actions
ADD CONSTRAINT fk_actions_nations
FOREIGN KEY (fk_Nations)
REFERENCES Nations(id)
ON DELETE SET NULL;

ALTER TABLE UnitOrders
ADD CONSTRAINT fk_unitOrders_nations
FOREIGN KEY (fk_Nations)
REFERENCES Nations(id)
ON DELETE SET NULL;

ALTER TABLE UnitOrders
ADD CONSTRAINT fk_unitOrders_unitTypes
FOREIGN KEY (fk_UnitTypes)
REFERENCES UnitTypes(id)
ON DELETE CASCADE;

ALTER TABLE AccessesToUnits
ADD CONSTRAINT fk_accessesToUnits_nations
FOREIGN KEY (fk_Nations)
REFERENCES Nations(id)
ON DELETE SET NULL;

ALTER TABLE AccessesToUnits
ADD CONSTRAINT fk_accessesToUnits_unitTypes
FOREIGN KEY (fk_UnitTypes)
REFERENCES UnitTypes(id)
ON DELETE CASCADE;

ALTER TABLE OfferedResources
ADD CONSTRAINT fk_offeredResources_resources
FOREIGN KEY (fk_Resources)
REFERENCES Resources(id)
ON DELETE CASCADE;

ALTER TABLE OfferedResources
ADD CONSTRAINT fk_offeredResources_tradeAgreements
FOREIGN KEY (fk_TradeAgreements)
REFERENCES TradeAgreements(id)
ON DELETE CASCADE;

ALTER TABLE WantedResources
ADD CONSTRAINT fk_wantedResources_resources
FOREIGN KEY (fk_Resources)
REFERENCES Resources(id)
ON DELETE CASCADE;

ALTER TABLE WantedResources
ADD CONSTRAINT fk_wantedResources_tradeAgreements
FOREIGN KEY (fk_TradeAgreements)
REFERENCES TradeAgreements(id)
ON DELETE CASCADE;

ALTER TABLE RelatedEvents
ADD CONSTRAINT fk_relatedEvents_nations
FOREIGN KEY (fk_Nations)
REFERENCES Nations(id)
ON DELETE SET NULL;

ALTER TABLE RelatedEvents
ADD CONSTRAINT fk_relatedEvents_events
FOREIGN KEY (fk_Events)
REFERENCES Events(id)
ON DELETE CASCADE;

ALTER TABLE UsedResources
ADD CONSTRAINT fk_usedResources_socialGroups
FOREIGN KEY (fk_SocialGroups)
REFERENCES SocialGroups(id)
ON DELETE SET NULL;

ALTER TABLE UsedResources
ADD CONSTRAINT fk_usedResources_resources
FOREIGN KEY (fk_Resources)
REFERENCES Resources(id)
ON DELETE CASCADE;

ALTER TABLE ProductionShares
ADD CONSTRAINT fk_productionShares_socialGroups
FOREIGN KEY (fk_SocialGroups)
REFERENCES SocialGroups(id)
ON DELETE SET NULL;

ALTER TABLE ProductionShares 
ADD CONSTRAINT fk_productionShares_resources
FOREIGN KEY (fk_Resources)
REFERENCES Resources(id)
ON DELETE CASCADE;

ALTER TABLE MaintenanceCosts
ADD CONSTRAINT fk_maintenanceCosts_unitTypes
FOREIGN KEY (fk_UnitTypes)
REFERENCES UnitTypes(id)
ON DELETE CASCADE;

ALTER TABLE MaintenanceCosts
ADD CONSTRAINT fk_maintenanceCosts_resources
FOREIGN KEY (fk_Resources)
REFERENCES Resources(id)
ON DELETE CASCADE;

-- UniqueTogether constraints
ALTER TABLE GrantedPermissions
ADD CONSTRAINT unique_user_permission
UNIQUE (fk_Users, fk_Permissions);

ALTER TABLE UnitOrders
ADD CONSTRAINT unique_nation_unit_order
UNIQUE (fk_Nations, fk_UnitTypes);

ALTER TABLE OwnedResources
ADD CONSTRAINT unique_nation_resource_owned
UNIQUE (fk_Nations, fk_Resources);

-- UserResources, productionshares, maintaincost, productioncost, locationresources, relatedevents