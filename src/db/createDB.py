from src.db.dbHelpers import create_connection

conn = create_connection()

cur = conn.cursor()
cur.execute("DROP TABLE IF EXISTS auctions;")
cur.execute("DROP TABLE IF EXISTS auctions_fts;")
cur.execute("DROP TRIGGER IF EXISTS auctions_fts_ai;")
cur.execute(
    """CREATE TABLE auctions (
    auctionEndDate INTEGER,
    bidCount INTEGER,
    biddingExtended INTEGER,
    buyNow REAL,
    companyId INTEGER,
    description TEXT,
    eventId INTEGER,
    eventItemId INTEGER NOT NULL PRIMARY KEY,
    fullSizeLocationPicture TEXT,
    highBid REAL,
    highBuyerId INTEGER,
    itemId INTEGER,
    lead TEXT,
    lotNumber TEXT,
    minBid REAL,
    priceRealized REAL,
    reserveSatisfied INTEGER,
    shippingOffered INTEGER
);
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
conn.commit()
conn.close()
