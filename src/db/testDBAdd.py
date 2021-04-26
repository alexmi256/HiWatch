import json
import logging
from pprint import pformat

from src.db.dbHelpers import AUCTION_INSERT_QUERY, create_connection
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
        c.executemany(AUCTION_INSERT_QUERY, data)
        conn.commit()
        conn.close()
    except Exception as ex:
        logger.error(ex)
