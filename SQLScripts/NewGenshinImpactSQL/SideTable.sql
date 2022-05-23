--WEAPONTYPE ROWS
INSERT INTO WeaponTypes (Type) VALUES 
    ('Sword'),
    ('Claymore'),
    ('Polearm'),
    ('Catalyst'),
    ('Bow');

--REGION ROWS
INSERT INTO Regions (Region) VALUES 
    ('Mondstadt'), 
    ('Liyue'),
    ('Inazuma'),
    ('Sumeru'),
    ('Fontaine'),
    ('Natlan'),
    ('Snezhnaya');

--ELEMENT ROWS
INSERT INTO Elements (Element) VALUES
    ('Pyro'),
    ('Hydro'), 
    ('Anemo'),
    ('Electro'), 
    ('Dendro'), 
    ('Cryo'),
    ('Geo');

--SECONDSTAT (for Weapons Table)
INSERT INTO SecondStats (Stat) VALUES 
    ('ATK'),
    ('HP'),
    ('DEF'),
    ('Physical DMG Bonus'),
    ('Energy Recharge'),
    ('Elemental Mastery'),
    ('CRIT DMG'),
    ('CRIT Rate');

--AVAILABILITY ROWS
INSERT INTO Availability (Days) VALUES
    (ARRAY['Sunday','Monday','Thursday']),
    (ARRAY['Sunday','Tuesday','Friday']),
    (ARRAY['Sunday','Wednesday','Saturday']);

--DOMAINNAME ROWS
INSERT INTO Domains (DomainName, Region_ID) VALUES 
    ('Forsaken Rift', 1 ),
    ('Cecilia Garden', 1 ),
    ('Taishan Mansion', 2 ),
    ('Hidden Palace of Lianshan Formula', 2 ),
    ('Violet Court', 3 ),
    ('Court of Flowing Sand', 3);

--DOMAINMATERIAL ROWS
INSERT INTO DomainMaterials (Material, MaterialType, Domain_ID, Availabilities) VALUES 
    ('Freedom','Character Ascension',1,1), 
    ('Decarabian','Weapon Ascension',2,1),
    ('Resistance', 'Character Ascension',1,2), 
    ('Boreal Wolf','Weapon Ascension',2,2),
    ('Balled', 'Character Ascension',1,3), 
    ('Dandelion Gladiator','Weapon Ascension',2,3),
    ('Prosperity', 'Character Ascension',3,1),
    ('Guyun','Weapon Ascension',4,1),
    ('Diligence','Character Ascension',3,2),
    ('Mist Veiled','Weapon Ascension',4,2),
    ('Gold','Character Ascension',3,3),
    ('Aerosiderite','Weapon Ascension',4,3),
    ('Tansience','Character Ascencion',5,1),
    ('Distant Sea','Weapon Ascension',3,1),
    ('Elegance','Character Ascension',6,2),
    ('Narukami','Weapon Ascension',6,2),
    ('Light','Character Ascension',5,3),
    ('Mask','Weapon Ascension',6,3);

--NOTE: columns to be added -> Values must also be updated