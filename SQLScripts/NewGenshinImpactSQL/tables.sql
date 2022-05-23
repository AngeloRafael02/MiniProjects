--NOTE: Set " to all Columns once filled with at least 1 row of data
--NOTE: Set references after making tables

--Side Tables
CREATE TABLE WeaponTypes (
    id SERIAL PRIMARY KEY,
    Type VARCHAR(10)
);
CREATE TABLE Regions (
    id SERIAL PRIMARY KEY,
    Region VARCHAR(20)
);
CREATE TABLE Elements (
    id SERIAL PRIMARY KEY,
    Element VARCHAR(20)
);
CREATE TABLE SecondStats (
    id SERIAL PRIMARY KEY,
    Stat VARCHAR(20)
);
CREATE TABLE Availability (
    id SERIAL PRIMARY KEY,
    Days VARCHAR(20)[]
);
CREATE TABLE Domains (
    id SERIAL PRIMARY KEY,
    DomainName VARCHAR(40),
    Region_ID INT REFERENCES Regions(id)
);
CREATE TABLE DomainMaterials (
    id SERIAL PRIMARY KEY,
    Material VARCHAR(20),
    MaterialType VARCHAR(20),
    Domain_ID INTEGER REFERENCES Domains(id),
    Availabilities INT REFERENCES Availability(id)
);

--Main Tables
CREATE TABLE Characters (
    id BIGSERIAL PRIMARY KEY,
    Name VARCHAR(50),
    Star INTEGER,
    Element_ID BIGINT REFERENCES Elements(id),
    WeaponType_ID BIGINT REFERENCES WeaponTypes(id),
    Region_ID BIGINT REFERENCES Regions(id),
    Domain_ID BIGINT REFERENCES Domains(id),
    DomainMaterial_ID BIGINT REFERENCES DomainMaterials(id),
    Availabilties INT REFERENCES Availability(id),
    ImgURL TEXT
);
CREATE TABLE Weapons (
    id BIGSERIAL PRIMARY KEY,
    Name VARCHAR(50),
    Star INTEGER,
    WeaponType_ID BIGINT REFERENCES WeaponTypes(id),
    SecondStat_ID BIGINT REFERENCES SecondStats(id),
    Domain_ID BIGINT REFERENCES Domains(id),
    DomainMaterial_ID BIGINT REFERENCES DomainMaterials(id),
    Availabilties INT REFERENCES Availability(id),
    ImgURL TEXT
);

--ALTERATIONS for rFUTURE COLUMN ADDING AND REFERENCES
