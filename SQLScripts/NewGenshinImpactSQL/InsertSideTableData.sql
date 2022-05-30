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
    ('ATK'),                --1
    ('HP'),                 --2
    ('DEF'),                --3
    ('Physical DMG Bonus'), --4
    ('Energy Recharge'),    --5
    ('Elemental Mastery'),  --6
    ('CRIT DMG'),           --7
    ('CRIT Rate');          --8

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
    ('Freedom','Character Ascension',1,1),          --1          
    ('Decarabian','Weapon Ascension',2,1),          --2
    ('Resistance', 'Character Ascension',1,2),      --3 
    ('Boreal Wolf','Weapon Ascension',2,2),         --4
    ('Balled', 'Character Ascension',1,3),          --5
    ('Dandelion Gladiator','Weapon Ascension',2,3), --6
    ('Prosperity', 'Character Ascension',3,1),      --7
    ('Guyun','Weapon Ascension',4,1),               --8
    ('Diligence','Character Ascension',3,2),        --9
    ('Mist Veiled','Weapon Ascension',4,2),         --10
    ('Gold','Character Ascension',3,3),             --11
    ('Aerosiderite','Weapon Ascension',4,3),        --12
    ('Tansience','Character Ascencion',5,1),        --13
    ('Distant Sea','Weapon Ascension',3,1),         --14
    ('Elegance','Character Ascension',6,2),         --15
    ('Narukami','Weapon Ascension',6,2),            --16
    ('Light','Character Ascension',5,3),            --17
    ('Mask','Weapon Ascension',6,3);                --18

--NOTE: columns to be added -> Values must also be updated
UPDATE Regions SET Character_Domain_ID = 1, Weapon_Domain_ID = 2 WHERE  region = 'Mondstadt';
UPDATE Regions SET Character_Domain_ID = 3, Weapon_Domain_ID = 4 WHERE  region = 'Liyue';
UPDATE Regions SET Character_Domain_ID = 5, Weapon_Domain_ID = 6 WHERE  region = 'Inazuma';
