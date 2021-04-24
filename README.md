# Intro
A tool to save auction ending prices for HiBid based sites

# How It Works
The way this script works is that it will check the first page of auctions and record prices.
If the last auction on this page ends in under 120 seconds, we will continue to check subsequent pages and record prices.
If not, then we will stop processing pages since we don't care about items that end later.

Usually when someone bids on an item it will extend the auction end time by 2min.

Thus, we only need to check auction prices periodically. Currently we recheck the first page based on the max(50 seconds, first auction end time - 30 seconds).

This should allow to capture the final price while not going overboard with making requests.


# Requirements
Python 3.9
SQLite with fts5

# TODO
- [ ] Experiment with filter to be `online` instead of `biddable`
- [ ] Check to make sure I'm not overwriting with empty prices
- [ ] Store currencies (CAD/USD) in a different table
- [ ] Change table structure
  - [x] Remove `auctionBeginDate` and make `auctionEndDate` an `int` based on UNIX time
  - [x] Remove `priceRealized`, `shippingOffered`, `reserveSatisfied`
  - [x] Save only `media id` and `checksum` for the image
  - [ ] Create table for auction states
  - [ ] Test `WITHOUT ROWID` for main table since I'm using something else
  - [ ] Merge the `lead` and `desciption` into one field
- [ ] Test out on main HiBid site
- [ ] Make website for viewing ended auctions
