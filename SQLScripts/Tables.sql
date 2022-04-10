CREATE TABLE characters (
    id BIGSERIAL NOT NULL PRIMARY KEY,
    name VARCHAR(50) NOT NULL,
    star INTEGER NOT NULL,
    element INTEGER NOT NULL,
    weapon INTEGER NOT NULL,
    region INTEGER NOT NULL,
    domainName INTEGER NOT NULL,
    ascensionmat INTEGER NOT NULL,
    ascensiondayid INTEGER NOT NULL
);

CREATE TABLE weapons (
    id BIGSERIAL NOT NULL PRIMARY KEY,
    name VARCHAR(50) NOT NULL,
    star INTEGER NOT NULL,
    weapon VARCHAR(50) NOT NULL,
    secondstat VARCHAR(20) NOT NULL,
    domainName VARCHAR(100) NOT NULL,
    ascensionmat VARCHAR(30) NOT NULL,
    ascensiondayid INTEGER NOT NULL
);

CREATE TABLE ascensionDays (
    id BIGSERIAL NOT NULL PRIMARY KEY,
    day VARCHAR(30)  --implement NOT NULL, After values is set
);

CREATE TABLE regions (
    id BIGSERIAL NOT NULL PRIMARY KEY,
    region VARCHAR(20) --implement NOT NULL, After values is set
);


CREATE TABLE elements (
    id BIGSERIAL NOT NULL PRIMARY KEY,
    element VARCHAR(10)  --implement NOT NULL, After values is set
);

CREATE TABLE characterAscension (
    id BIGSERIAL NOT NULL PRIMARY KEY,
    material VARCHAR(20)  --implement NOT NULL, After values is set
);

CREATE TABLE weaponAscension (
    id BIGSERIAL NOT NULL PRIMARY KEY,
    material VARCHAR(20)
);

CREATE TABLE DomainName (
    id BIGSERIAL NOT NULL PRIMARY KEY,
    domain VARCHAR(40)  --implement NOT NULL, After values is set
);

CREATE TABLE Weapontype (
    id BIGSERIAL NOT NULL PRIMARY KEY,
    type VARCHAR(10)  --implement NOT NULL, After values is set
);