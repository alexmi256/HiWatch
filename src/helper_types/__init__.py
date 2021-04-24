from typing import TypedDict, Union

ParsedAuction = list[Union[str, int, float]]
ParsedAuctions = list[ParsedAuction]


class AuctionResult(TypedDict):
    auctionEndDate: int
    bidCount: int
    biddingExtended: int
    buyNow: float
    companyId: int
    description: str
    eventId: int
    eventItemId: int
    pictureId: int
    pictureChecksum: str
    highBid: float
    highBuyerId: int
    itemId: int
    lead: str
    lotNumber: str
    minBid: float
