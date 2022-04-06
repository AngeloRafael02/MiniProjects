    --EXAMPLES OF SQL:
    --FROM a genshin impact database i made
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