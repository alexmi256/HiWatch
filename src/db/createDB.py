from src.db.dbHelpers import create_connection
from src.constants import STATES

conn = create_connection()

cur = conn.cursor()
cur.execute("DROP TABLE IF EXISTS auctions;")
cur.execute("DROP TABLE IF EXISTS auctions_fts;")
cur.execute("DROP TABLE IF EXISTS states;")
cur.execute("DROP TRIGGER IF EXISTS auctions_fts_ai;")
cur.execute(
    """CREATE TABLE auctions (
    auctionEndDate INTEGER,
    auctionState INTEGER,
    bidCount INTEGER,
    buyNow REAL,
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
"""
)
# AFAICT While I can create an fts table based on another table, I will still need to updated the fts table itself
# once new values are added into the original table. TBH I don't know why I'm even bothering to do this if I still
# need to create the triggers.
# https://sqlite.org/fts5.html#external_content_tables
cur.execute(
    """CREATE VIRTUAL TABLE auctions_fts USING fts5(
        lead,
        description,
        content=auctions,
        content_rowid=eventItemId
    );
    """
)
cur.execute(
    """CREATE TRIGGER auctions_fts_ai AFTER INSERT ON auctions BEGIN
  INSERT INTO auctions_fts(rowid, lead, description) VALUES (new.eventItemId, new.lead, new.description);
END;"""
)
cur.execute(
    """CREATE TABLE states (
    id INTEGER NOT NULL PRIMARY KEY,
    twoLetterCode TEXT
)   WITHOUT ROWID;
"""
)
cur.executemany('INSERT INTO states VALUES(?,?);', [[v, k] for k, v in STATES.items()])
conn.commit()
conn.close()
