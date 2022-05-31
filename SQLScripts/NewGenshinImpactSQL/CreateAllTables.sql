--NOTE: Set " to all Columns once filled with at least 1 row of data
--NOTE: Set references after making tables

--Side Tables
CREATE TABLE WeaponTypes (
    id SERIAL PRIMARY KEY,
    Type VARCHAR(10) NOT NULL
);
CREATE TABLE Regions (
    id SERIAL PRIMARY KEY,
    Region VARCHAR(20) NOT NULL
);
CREATE TABLE Elements (
    id SERIAL PRIMARY KEY,
    Element VARCHAR(20) NOT NULL
);
CREATE TABLE SecondStats (
    id SERIAL PRIMARY KEY,
    Stat VARCHAR(20) NOT NULL
);
CREATE TABLE Availability (
    id SERIAL PRIMARY KEY,
    Days VARCHAR(20)[] NOT NULL
);
CREATE TABLE AscensionDomains (
    id SERIAL PRIMARY KEY,
    DomainName VARCHAR(40) NOT NULL,
    Region_ID INT REFERENCES Regions(id) NOT NULL
);
CREATE TABLE CharacterDomainMaterials (
    id SERIAL PRIMARY KEY,
    Material VARCHAR(20) NOT NULL,
    Domain_ID INTEGER REFERENCES Domains(id) NOT NULL,
    Availabilities INT REFERENCES Availability(id) NOT NULL
);
CREATE TABLE WeaponDomainMaterials (
    id SERIAL PRIMARY KEY,
    Material VARCHAR(20) NOT NULL,
    Domain_ID INTEGER REFERENCES Domains(id) NOT NULL,
    Availabilities INT REFERENCES Availability(id) NOT NULL
);

--Main Tables
CREATE TABLE Characters (
    id BIGSERIAL PRIMARY KEY,
    Name VARCHAR(50) NOT NULL,
    Star INTEGER NOT NULL,
    Element_ID BIGINT REFERENCES Elements(id) NOT NULL,
    WeaponType_ID BIGINT REFERENCES WeaponTypes(id) NOT NULL,
    Region_ID BIGINT REFERENCES Regions(id) NOT NULL,
    Domain_ID BIGINT REFERENCES Domains(id) NOT NULL,
    DomainMaterial_ID BIGINT REFERENCES CharacterDomainMaterials(id) NOT NULL,
    Availabilties INT REFERENCES Availability(id) NOT NULL,
    ImgURL TEXT NOT NULL
);
CREATE TABLE Weapons (
    id BIGSERIAL PRIMARY KEY,
    Name VARCHAR(50) NOT NULL,
    Star INTEGER NOT NULL,
    WeaponType_ID BIGINT REFERENCES WeaponTypes(id) NOT NULL,
    SecondStat_ID BIGINT REFERENCES SecondStats(id NOT NULL),
    Domain_ID BIGINT REFERENCES Domains(id) NOT NULL,
    DomainMaterial_ID BIGINT REFERENCES WeaponDomainMaterials(id) NOT NULL,
    Availabilties INT REFERENCES Availability(id) NOT NULL,
    ImgURL TEXT NOT NULL
);

--ALTERATIONS for COLUMN and REFERENCES Adding

ALTER TABLE Regions
    ADD COLUMN Character_Domain_ID BIGINT REFERENCES Domains(id) NOT NULL, --reference only Character Domains, Make column NULLABLE
    ADD COLUMN Weapon_Domain_ID BIGINT REFERENCES Domains(id) NOT NULL; --reference only weapon domains, Make column NULLABLE
