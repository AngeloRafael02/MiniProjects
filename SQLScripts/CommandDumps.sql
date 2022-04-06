--VIEW: easier shortcut commands

--RAW
SELECT characters.name, characters.star, elements.element, weapontype.type, regions.region, domainname.domain, characterascension.material, ascensiondays.day FROM characters 
    INNER JOIN ascensiondays ON characters.ascensiondayid = ascensiondays.id 
    JOIN regions ON characters.region = regions.id 
    JOIN elements ON characters.element = elements.id 
    JOIN weapontype ON characters.weapon = weapontype.id
    JOIN domainname ON characters.domainname = domainname.id
    JOIN characterascension ON characters.ascensionmat = characterascension.id
    WHERE characters.ascensiondayid = 1 ORDER BY characters.id ASC;

SELECT characters.name, characters.star, elements.element, weapontype.type, regions.region, domainname.domain, characterascension.material, ascensiondays.day FROM characters 
    INNER JOIN ascensiondays ON characters.ascensiondayid = ascensiondays.id 
    JOIN regions ON characters.region = regions.id 
    JOIN elements ON characters.element = elements.id 
    JOIN weapontype ON characters.weapon = weapontype.id
    JOIN domainname ON characters.domainname = domainname.id
    JOIN characterascension ON characters.ascensionmat = characterascension.id
    WHERE characters.ascensiondayid = 2 ORDER BY characters.id ASC;

SELECT characters.name, characters.star, elements.element, weapontype.type, regions.region, domainname.domain, characterascension.material, ascensiondays.day FROM characters 
    INNER JOIN ascensiondays ON characters.ascensiondayid = ascensiondays.id 
    JOIN regions ON characters.region = regions.id 
    JOIN elements ON characters.element = elements.id 
    JOIN weapontype ON characters.weapon = weapontype.id
    JOIN domainname ON characters.domainname = domainname.id
    JOIN characterascension ON characters.ascensionmat = characterascension.id
    WHERE characters.ascensiondayid = 3 ORDER BY characters.id ASC;

SELECT weapons.name, weapons.star, regions.region, weapons.domainname, weapons.ascensionmat, ascensiondays.day FROM weapons INNER JOIN ascensiondays ON weapons.ascensiondayid = ascensiondays.id JOIN regions ON weapons.region = regions.id WHERE weapons.ascensiondayid = 1 ORDER BY weapons.id ASC;
SELECT weapons.name, weapons.star, regions.region, weapons.domainname, weapons.ascensionmat, ascensiondays.day FROM weapons INNER JOIN ascensiondays ON weapons.ascensiondayid = ascensiondays.id JOIN regions ON weapons.region = regions.id WHERE weapons.ascensiondayid = 2 ORDER BY weapons.id ASC;
SELECT weapons.name, weapons.star, regions.region, weapons.domainname, weapons.ascensionmat, ascensiondays.day FROM weapons INNER JOIN ascensiondays ON weapons.ascensiondayid = ascensiondays.id JOIN regions ON weapons.region = regions.id WHERE weapons.ascensiondayid = 3 ORDER BY weapons.id ASC;

--VIEW
CREATE VIEW day1characters AS SELECT characters.name, characters.star, elements.element, weapontype.type, regions.region, domainname.domain, characterascension.material, ascensiondays.day FROM characters INNER JOIN ascensiondays ON characters.ascensiondayid = ascensiondays.id JOIN regions ON characters.region = regions.id JOIN elements ON characters.element = elements.id JOIN weapontype ON characters.weapon = weapontype.id JOIN domainname ON characters.domainname = domainname.id JOIN characterascension ON characters.ascensionmat = characterascension.id WHERE characters.ascensiondayid = 1 ORDER BY characters.id ASC;
CREATE VIEW day2characters AS SELECT characters.name, characters.star, elements.element, weapontype.type, regions.region, domainname.domain, characterascension.material, ascensiondays.day FROM characters INNER JOIN ascensiondays ON characters.ascensiondayid = ascensiondays.id JOIN regions ON characters.region = regions.id JOIN elements ON characters.element = elements.id JOIN weapontype ON characters.weapon = weapontype.id JOIN domainname ON characters.domainname = domainname.id JOIN characterascension ON characters.ascensionmat = characterascension.id WHERE characters.ascensiondayid = 2 ORDER BY characters.id ASC;
CREATE VIEW day3characters AS SELECT characters.name, characters.star, elements.element, weapontype.type, regions.region, domainname.domain, characterascension.material, ascensiondays.day FROM characters INNER JOIN ascensiondays ON characters.ascensiondayid = ascensiondays.id JOIN regions ON characters.region = regions.id JOIN elements ON characters.element = elements.id JOIN weapontype ON characters.weapon = weapontype.id JOIN domainname ON characters.domainname = domainname.id JOIN characterascension ON characters.ascensionmat = characterascension.id WHERE characters.ascensiondayid = 3 ORDER BY characters.id ASC;

CREATE VIEW day1weapons AS SELECT weapons.name, weapons.star, regions.region, weapons.domainname, weapons.ascensionmat, ascensiondays.day FROM weapons INNER JOIN ascensiondays ON weapons.ascensiondayid = ascensiondays.id JOIN regions ON weapons.region = regions.id WHERE weapons.ascensiondayid = 1 ORDER BY weapons.id ASC;
CREATE VIEW day2weapons AS SELECT weapons.name, weapons.star, regions.region, weapons.domainname, weapons.ascensionmat, ascensiondays.day FROM weapons INNER JOIN ascensiondays ON weapons.ascensiondayid = ascensiondays.id JOIN regions ON weapons.region = regions.id WHERE weapons.ascensiondayid = 2 ORDER BY weapons.id ASC;
CREATE VIEW day3weapons AS SELECT weapons.name, weapons.star, regions.region, weapons.domainname, weapons.ascensionmat, ascensiondays.day FROM weapons INNER JOIN ascensiondays ON weapons.ascensiondayid = ascensiondays.id JOIN regions ON weapons.region = regions.id WHERE weapons.ascensiondayid = 3 ORDER BY weapons.id ASC;
--CALL
SELECT * FROM day1characters;
SElECT * FROM day2characters;
SELECT * FROM day3characters;
SELECT * FROM day1weapons;
SELECT * FROM day2weapons;
SELECT * FROM day3weapons;


--Make NOT NULL -> NULL and vice versa
ALTER TABLE tablename ALTER COLUMN columnname DROP NOT NULL;
ALTER TABLE tablename ALTER COLUMN columnname SET NOT NULL;
--empty columns
UPDATE tablename SET columnname = NULL;
--change column data type
ALTER TABLE characters ALTER COLUMN element TYPE integer USING element::integer;

--Pyro
UPDATE characters SET element = 1 WHERE id IN (1,6,11,16,21,24,29,31,36,41);
--Hydro
UPDATE characters SET element = 2 WHERE id IN (4,8,18,23,40,47);
--Anemo
UPDATE characters SET element = 3 WHERE id IN (14,15,20,28,33,35);
--Electro
UPDATE characters SET element = 4 WHERE id IN (3,5,7,10,19,38,39,46);
--Cryo
UPDATE characters SET element = 6 WHERE id IN (2,13,17,22,27,30,32,34,37,45);
--Geo
UPDATE characters SET element = 7 WHERE id IN (9,12,25,26,42,43,44);

--ascensionmat
UPDATE characters SET ascensionmat = 1 WHERE domainname = 'forsaken_rift' AND ascensiondayid = 1;
UPDATE characters SET ascensionmat = 2 WHERE domainname = 'forsaken_rift' AND ascensiondayid = 2;
UPDATE characters SET ascensionmat = 3 WHERE domainname = 'forsaken_rift' AND ascensiondayid = 3;
UPDATE characters SET ascensionmat = 4 WHERE domainname = 'taishan_mansion' AND ascensiondayid = 1;
UPDATE characters SET ascensionmat = 5 WHERE domainname = 'taishan_mansion' AND ascensiondayid = 2;
UPDATE characters SET ascensionmat = 6 WHERE domainname = 'taishan_mansion' AND ascensiondayid = 3;
UPDATE characters SET ascensionmat = 7 WHERE domainname = 'violet_court' AND ascensiondayid = 1;
UPDATE characters SET ascensionmat = 8 WHERE domainname = 'violet_court' AND ascensiondayid = 2;
UPDATE characters SET ascensionmat = 9 WHERE domainname = 'violet_court' AND ascensiondayid = 3;

--domainname
UPDATE characters SET domainname = 1 WHERE region = 1;
UPDATE characters SET domainname = 2 WHERE region = 2;
UPDATE characters SET domainname = 3 WHERE region = 3;

--CHAR.WEAPON
--sword
UPDATE characters SET weapon = 1 WHERE id IN(2,8,11,15,17,19,26,33,34,47);
--claymore
UPDATE characters SET weapon = 2 WHERE id IN(5,7,12,13,16,24,32,35,43);
--polearm
UPDATE characters SET weapon = 3 WHERE id IN(6,25,28,29,30,39,41,44,45);
--catalyst
UPDATE characters SET weapon = 4 WHERE id IN(3,4,9,14,18,21,31,40,46);
--bow
UPDATE characters SET weapon = 5 WHERE id IN(1,10,20,22,23,27,36,37,38,42);
































--OLD DUMPS
    --OLD VIEW SCRIPTS
    --RAW
SELECT characters.name, characters.star, regions.region, characters.domainname, characters.ascensionmat, ascensiondays.day FROM characters INNER JOIN ascensiondays ON characters.ascensiondayid = ascensiondays.id JOIN regions ON characters.region = regions.id WHERE characters.ascensiondayid = 1 ORDER BY characters.id ASC;
SELECT characters.name, characters.star, regions.region, characters.domainname, characters.ascensionmat, ascensiondays.day FROM characters INNER JOIN ascensiondays ON characters.ascensiondayid = ascensiondays.id JOIN regions ON characters.region = regions.id WHERE characters.ascensiondayid = 2 ORDER BY characters.id ASC;
SELECT characters.name, characters.star, regions.region, characters.domainname, characters.ascensionmat, ascensiondays.day FROM characters INNER JOIN ascensiondays ON characters.ascensiondayid = ascensiondays.id JOIN regions ON characters.region = regions.id WHERE characters.ascensiondayid = 3 ORDER BY characters.id ASC;
SELECT weapons.name, weapons.star, regions.region, weapons.domainname, weapons.ascensionmat, ascensiondays.day FROM weapons INNER JOIN ascensiondays ON weapons.ascensiondayid = ascensiondays.id JOIN regions ON weapons.region = regions.id WHERE weapons.ascensiondayid = 1 ORDER BY weapons.id ASC;
SELECT weapons.name, weapons.star, regions.region, weapons.domainname, weapons.ascensionmat, ascensiondays.day FROM weapons INNER JOIN ascensiondays ON weapons.ascensiondayid = ascensiondays.id JOIN regions ON weapons.region = regions.id WHERE weapons.ascensiondayid = 2 ORDER BY weapons.id ASC;
SELECT weapons.name, weapons.star, regions.region, weapons.domainname, weapons.ascensionmat, ascensiondays.day FROM weapons INNER JOIN ascensiondays ON weapons.ascensiondayid = ascensiondays.id JOIN regions ON weapons.region = regions.id WHERE weapons.ascensiondayid = 3 ORDER BY weapons.id ASC;
    --VIEW
CREATE VIEW day1characters AS SELECT characters.name, characters.star, regions.region, characters.domainname, characters.ascensionmat, ascensiondays.day FROM characters INNER JOIN ascensiondays ON characters.ascensiondayid = ascensiondays.id JOIN regions ON characters.region = regions.id WHERE characters.ascensiondayid = 1 ORDER BY characters.id ASC;
CREATE VIEW day2characters AS SELECT characters.name, characters.star, regions.region, characters.domainname, characters.ascensionmat, ascensiondays.day FROM characters INNER JOIN ascensiondays ON characters.ascensiondayid = ascensiondays.id JOIN regions ON characters.region = regions.id WHERE characters.ascensiondayid = 2 ORDER BY characters.id ASC;
CREATE VIEW day3characters AS SELECT characters.name, characters.star, regions.region, characters.domainname, characters.ascensionmat, ascensiondays.day FROM characters INNER JOIN ascensiondays ON characters.ascensiondayid = ascensiondays.id JOIN regions ON characters.region = regions.id WHERE characters.ascensiondayid = 3 ORDER BY characters.id ASC;
CREATE VIEW day1weapons AS SELECT weapons.name, weapons.star, regions.region, weapons.domainname, weapons.ascensionmat, ascensiondays.day FROM weapons INNER JOIN ascensiondays ON weapons.ascensiondayid = ascensiondays.id JOIN regions ON weapons.region = regions.id WHERE weapons.ascensiondayid = 1 ORDER BY weapons.id ASC;
CREATE VIEW day2weapons AS SELECT weapons.name, weapons.star, regions.region, weapons.domainname, weapons.ascensionmat, ascensiondays.day FROM weapons INNER JOIN ascensiondays ON weapons.ascensiondayid = ascensiondays.id JOIN regions ON weapons.region = regions.id WHERE weapons.ascensiondayid = 2 ORDER BY weapons.id ASC;
CREATE VIEW day3weapons AS SELECT weapons.name, weapons.star, regions.region, weapons.domainname, weapons.ascensionmat, ascensiondays.day FROM weapons INNER JOIN ascensiondays ON weapons.ascensiondayid = ascensiondays.id JOIN regions ON weapons.region = regions.id WHERE weapons.ascensiondayid = 3 ORDER BY weapons.id ASC;
    --CALL
SELECT * FROM day1characters;
SElECT * FROM day2characters;
SELECT * FROM day3characters;
    --DROP THESE for imporvement: add stars and region
SELECT * FROM day1weapons;
SELECT * FROM day2weapons;
SELECT * FROM day3weapons;