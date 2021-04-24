import logging
from pprint import pformat
from typing import Any, Optional
from urllib.parse import urlparse, parse_qs

import arrow

from src.helper_types import ParsedAuction, ParsedAuctions

logger = logging.getLogger(__name__)


def parse_picture_url(url: str) -> tuple[Optional[int], Optional[str]]:
    """
    Parses out the picture id and checksum from the given url
    Example:
        https://media.sandhills.com/img.axd?id=12345&wid=&p=&ext=&w=0&h=0&t=&lp=&c=True&wt=False&sz=Max&rt=0&checksum=QWERTYUIOP
        will return [12345, QWERTYUIOP]
    :param url:
    :return:
    """
    params = parse_qs(urlparse(url).query)
    pid = int(params['id'][0]) if 'id' in params and params['id'] else None
    checksum = params['checksum'][0] if 'checksum' in params and params['checksum'] else None

    return pid, checksum



def parse_responses(response_data: dict[str, Any]) -> ParsedAuctions:
    """
    Parses the response data dictionary into a list where the values can be inserted into SQLite
    :return: A list of parsed auction items
    """
    data = []
    for result in response_data["results"]:
        try:
            data.append(parse_auction_result_list(result))
        except Exception as err:
            logger.error(f"Failed to parse result: {pformat(result)}\n{err}")

    return data


def parse_auction_result_list(result: dict[str, Any]) -> ParsedAuction:
    """
    Parses a single auction result into an SQLite friendly format

    :param result: The dict of a single auction
    :return: A list of the single auction with data in the following order
        auctionEndDate
        bidCount
        biddingExtended
        buyNow
        companyId
        description
        eventId
        eventItemId
        pictureId
        pictureChecksum
        highBid
        highBuyerId
        itemId
        lead
        lotNumber
        minBid
    """
    picture_id, picture_checksum = parse_picture_url(result.get("featuredPicture", {}).get("fullSizeLocation"))
    return [
        arrow.get(result.get("auctionEndDate", ""), "M/D/YYYY").int_timestamp,
        result.get("lotStatus", {}).get("bidCount", None),
        int(result.get("lotStatus", {}).get("biddingExtended", False) is True),
        result.get("lotStatus", {}).get("buyNow", None),
        result.get("companyId", None),
        result.get("description", None),
        result.get("eventId", None),
        result.get("eventItemId", None),
        picture_id,
        picture_checksum,
        result.get("lotStatus", {}).get("highBid", None),
        int(result.get("lotStatus", {}).get("highBuyerId", None)),
        result.get("itemId", None),
        result.get("lead", None),
        result.get("lotNumber", None),
        result.get("lotStatus", {}).get("minBid", None),
    ]
