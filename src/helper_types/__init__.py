from typing import TypedDict, Union

ParsedAuction = list[Union[str, int, float]]
ParsedAuctions = list[ParsedAuction]


class AuctionResult(TypedDict):
    auctionBeginDate: str
    auctionEndDate: str
    bidCount: int
    biddingExtended: int
    buyNow: float
    companyId: int
    description: str
    eventId: int
    eventItemId: int
    fullSizeLocationPicture: str
    highBid: float
    highBuyerId: int
    itemId: int
    lead: str
    lotNumber: str
    minBid: float
    priceRealized: float
    reserveSatisfied: int
    shippingOffered: int
