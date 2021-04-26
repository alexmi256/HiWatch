DROP TABLE IF EXISTS auctions;
DROP TABLE IF EXISTS auctions_fts;
DROP TABLE IF EXISTS states;
DROP TRIGGER IF EXISTS auctions_fts_ai;

CREATE TABLE auctions (
    auctionEndDate INTEGER,
    auctionState INTEGER,
    bidCount INTEGER,
    companyId INTEGER,
    description TEXT,
    eventId INTEGER,
    eventItemId INTEGER NOT NULL PRIMARY KEY,
    pictureId INTEGER,
    pictureChecksum TEXT,
    highBid REAL,
    highBuyerId INTEGER,
    itemId INTEGER,
    lead TEXT,
    lotNumber TEXT,
    minBid REAL
)   WITHOUT ROWID;

CREATE VIRTUAL TABLE auctions_fts USING fts5(
    lead,
    description,
    content=auctions,
    content_rowid=eventItemId
);

CREATE TRIGGER auctions_fts_ai AFTER INSERT ON auctions BEGIN
  INSERT INTO auctions_fts(rowid, lead, description) VALUES (new.eventItemId, new.lead, new.description);
END;

CREATE TABLE states (
    id INTEGER NOT NULL PRIMARY KEY,
    twoLetterCode TEXT
)   WITHOUT ROWID;

INSERT INTO states
VALUES
    (1, 'AL'),
    (2, 'AK'),
    (3, 'AS'),
    (4, 'AZ'),
    (5, 'AR'),
    (6, 'CA'),
    (7, 'CO'),
    (8, 'CT'),
    (9, 'DE'),
    (10, 'DC'),
    (11, 'FL'),
    (12, 'GA'),
    (13, 'GU'),
    (14, 'HI'),
    (15, 'ID'),
    (16, 'IL'),
    (17, 'IN'),
    (18, 'IA'),
    (19, 'KS'),
    (20, 'KY'),
    (21, 'LA'),
    (22, 'ME'),
    (23, 'MD'),
    (24, 'MA'),
    (25, 'MI'),
    (26, 'MN'),
    (27, 'MS'),
    (28, 'MO'),
    (29, 'MT'),
    (30, 'NE'),
    (31, 'NV'),
    (32, 'NH'),
    (33, 'NJ'),
    (34, 'NM'),
    (35, 'NY'),
    (36, 'NC'),
    (37, 'ND'),
    (38, 'MP'),
    (39, 'OH'),
    (40, 'OK'),
    (41, 'OR'),
    (42, 'PA'),
    (43, 'PR'),
    (44, 'RI'),
    (45, 'SC'),
    (46, 'SD'),
    (47, 'TN'),
    (48, 'TX'),
    (49, 'UT'),
    (50, 'VT'),
    (51, 'VA'),
    (52, 'VI'),
    (53, 'WA'),
    (54, 'WV'),
    (55, 'WI'),
    (56, 'WY'),
    (57, 'AB'),
    (58, 'BC'),
    (59, 'MB'),
    (60, 'NB'),
    (61, 'NL'),
    (62, 'NT'),
    (63, 'NS'),
    (64, 'NU'),
    (65, 'ON'),
    (66, 'PE'),
    (67, 'QC'),
    (68, 'SK'),
    (69, 'YT');
