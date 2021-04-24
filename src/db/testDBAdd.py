import json
import logging
from pprint import pformat

from src.db.dbHelpers import create_connection
from src.response_parser import parse_responses

logging.basicConfig(level=logging.INFO)

logger = logging.getLogger(__name__)


with open("../../response.json") as json_file:
    save_data = json.load(json_file)
    data = parse_responses(save_data)
    for item in data:
        logger.debug(pformat(item))
    try:
        conn = create_connection()
        c = conn.cursor()
        c.executemany(
            """INSERT INTO auctions VALUES(?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?) ON CONFLICT(eventItemId)
             DO UPDATE SET
                bidCount=excluded.bidCount,
                biddingExtended=excluded.biddingExtended,
                highBid=excluded.highBid,
                highBuyerId=excluded.highBuyerId,
                minBid=excluded.minBid,
                priceRealized=excluded.priceRealized,
                reserveSatisfied=excluded.reserveSatisfied
        """,
            data,
        )
        conn.commit()
        conn.close()
    except Exception as ex:
        logger.error(ex)
