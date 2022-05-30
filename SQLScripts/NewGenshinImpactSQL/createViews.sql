--CHARACTERS VIEWS
--All Days Characters
CREATE VIEW AllCharacters AS 
SELECT characters.id, name, star, Elements.Element, WeaponTypes.Type, Regions.Region, Domains.DomainName, DomainMaterials.Material, Availability.Days, ImgURL
    FROM Characters
    JOIN Elements ON Characters.Element_id = Elements.id
    JOIN WeaponTypes ON Characters.WeaponType_id = WeaponTypes.id
    JOIN Regions ON Characters.Region_id = Regions.id
    JOIN Domains ON Characters.Domain_id = Domains.id
    JOIN DomainMaterials ON Characters.DomainMaterial_id = DomainMaterials.id
    JOIN Availability ON Characters.Availabilties = Availability.id
    WHERE Availabilties IN (1,2,3)
    ORDER BY characters.id ASC;
--Monday, Thursday, Sunday Characters
CREATE VIEW Day1Characters AS 
SELECT characters.id, name, star, Elements.Element, WeaponTypes.Type, Regions.Region, Domains.DomainName, DomainMaterials.Material, Availability.Days, ImgURL
    FROM Characters
    JOIN Elements ON Characters.Element_id = Elements.id
    JOIN WeaponTypes ON Characters.WeaponType_id = WeaponTypes.id
    JOIN Regions ON Characters.Region_id = Regions.id
    JOIN Domains ON Characters.Domain_id = Domains.id
    JOIN DomainMaterials ON Characters.DomainMaterial_id = DomainMaterials.id
    JOIN Availability ON Characters.Availabilties = Availability.id
    WHERE Availabilties = 1 
    ORDER BY characters.id ASC;
--Tuesday, Friday, Sunday Characters
CREATE VIEW Day2Characters AS 
SELECT characters.id, name, star, Elements.Element, WeaponTypes.Type, Regions.Region, Domains.DomainName, DomainMaterials.Material, Availability.Days , ImgURL
    FROM Characters
    JOIN Elements ON Characters.Element_id = Elements.id
    JOIN WeaponTypes ON Characters.WeaponType_id = WeaponTypes.id
    JOIN Regions ON Characters.Region_id = Regions.id
    JOIN Domains ON Characters.Domain_id = Domains.id
    JOIN DomainMaterials ON Characters.DomainMaterial_id = DomainMaterials.id
    JOIN Availability ON Characters.Availabilties = Availability.id
    WHERE Availabilties = 2 
    ORDER BY characters.id ASC;
--Wednesday, Saturday, Sunday Characters
CREATE VIEW Day3Characters AS 
SELECT characters.id, name, star, Elements.Element, WeaponTypes.Type, Regions.Region, Domains.DomainName, DomainMaterials.Material, Availability.Days, ImgURL
    FROM Characters
    JOIN Elements ON Characters.Element_id = Elements.id
    JOIN WeaponTypes ON Characters.WeaponType_id = WeaponTypes.id
    JOIN Regions ON Characters.Region_id = Regions.id
    JOIN Domains ON Characters.Domain_id = Domains.id
    JOIN DomainMaterials ON Characters.DomainMaterial_id = DomainMaterials.id
    JOIN Availability ON Characters.Availabilties = Availability.id
    WHERE Availabilties = 3
    ORDER BY characters.id ASC;