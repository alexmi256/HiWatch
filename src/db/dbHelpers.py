import logging
import sqlite3

logger = logging.getLogger(__name__)


def create_connection(db_file="auctions.db"):
    """create a database connection to the SQLite database
        specified by the db_file
    :param db_file: database file
    :return: Connection object
    """
    return sqlite3.connect(db_file)


# Query to search for items:
# SELECT auctionEndDate,bidCount,description,eventItemId,highBid,lead,minBid FROM auctions JOIN (SELECT rowid AS eventItemId FROM auctions_fts('mirror')) USING(eventItemId);

AUCTION_INSERT_QUERY = """
INSERT INTO auctions
VALUES(?,?,?,?,?,?,?,?,?,?,?,?,?,?,?) ON CONFLICT(eventItemId) DO
UPDATE
SET bidCount=excluded.bidCount,
    highBid=excluded.highBid,
    highBuyerId=excluded.highBuyerId,
    minBid=excluded.minBid
"""
