#!/usr/bin/env python3.9
import argparse
import logging
import sqlite3
import time
from contextlib import closing

import requests

from src.constants import COOKIES, GLOBAL, HEADERS, PAYLOAD, URLS
from src.db.dbHelpers import AUCTION_INSERT_QUERY
from src.helper_types import ParsedAuctions
from src.response_parser import parse_responses

logging.basicConfig(level=logging.DEBUG)
logger = logging.getLogger(__name__)


class AuctionParser:
    def __init__(self, site, db_location):
        self.site = site
        self.db_location = db_location
        while True:
            sleep_time = max(50, self.parse_pages() - 30)
            logger.info(f"Sleeping for {sleep_time} seconds until performing next check")
            time.sleep(sleep_time)

    def save_auctions(self, auctions: ParsedAuctions):
        """
        Saves the auctions to the database

        :param auctions: A list of parsed auctions
        :return:
        """
        try:
            logger.info(f"Saving {len(auctions)} auction items")
            with closing(sqlite3.connect(self.db_location)) as conn:
                with conn:
                    with closing(conn.cursor()) as cursor:
                        cursor.executemany(AUCTION_INSERT_QUERY, auctions)
        except Exception as e:
            logger.error("Failed to save data")
            logger.error(e)

    def parse_page(self, number: object) -> tuple[ParsedAuctions, bool, int]:
        """
        Parses the results of an auction page

        :param number: Number of the page to start parsing at
        :return: A tuple containing: The parsed results list, if the next page should be parsed, time remaining for the
            first auction in the list
        """
        logger.info(f"Parsing page #{number}")
        new_payload = PAYLOAD.copy()
        new_payload["pn"] = number
        response = requests.get(
            URLS[self.site], params=new_payload, headers=HEADERS, cookies=COOKIES, allow_redirects=False
        )
        response.raise_for_status()
        response_data = response.json()

        if "results" not in response_data or len(response_data["results"]) == 0:
            raise Exception("None or Empty results found in response data")

        parsed_data = parse_responses(response_data)
        first_item_end_time = response_data["results"][0]["lotStatus"]["timeLeftSeconds"]
        last_item_end_time = response_data["results"][-1]["lotStatus"]["timeLeftSeconds"]
        parse_next_page = last_item_end_time < 120.0
        logger.debug(
            f"Last item of page {number} ends in {last_item_end_time} seconds. Will parse next?: {parse_next_page}"
        )
        first_auction_ends = int(first_item_end_time)

        return parsed_data, parse_next_page, first_auction_ends

    def parse_pages(self) -> int:
        """
        Parses auction pages until and saves them to the database

        :return: Number of seconds until the first auction expires
        """
        logger.info(f"Parsing all pages")
        all_items = []
        parse_next_page = True
        page_number = 1
        first_page_auction_ends = None

        while parse_next_page:
            try:
                items, parse_next_page, first_auction_ends = self.parse_page(page_number)
                if first_page_auction_ends is None:
                    logger.debug(f"First auction ends in {first_auction_ends} seconds")
                    first_page_auction_ends = first_auction_ends
                all_items.extend(items)
                page_number += 1
            except Exception as e:
                logger.error(f"Failed to parse page #{page_number}, will quit loop")
                logger.error(e)
                parse_next_page = False
                if first_page_auction_ends is None:
                    logger.warning(f"Failed to know when to perform next check, defaulting to 60s")
                    first_page_auction_ends = 50

        self.save_auctions(all_items)
        return first_page_auction_ends


if __name__ == "__main__":
    parser = argparse.ArgumentParser()
    parser.add_argument(
        "site", type=str, choices=[GLOBAL, "ontario"], default=GLOBAL, help="Site to parse results from"
    )
    parser.add_argument("db", default="src/db/auctions.db", type=str, help="Path to the SQLite database")
    parser.add_argument("-v", "--verbosity", action="count", default=0, help="Increase output verbosity")
    args = parser.parse_args()
    # if args.verbosity == 1:
    #     logger.setLevel(logging.INFO)
    # elif args.verbosity == 2:
    #     logger.setLevel(logging.DEBUG)
    # elif args.verbosity > 2:
    #     logger.setLevel(logging.NOTSET)

    AuctionParser(args.site, args.db)
