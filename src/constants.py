URLS = {"ontario": "https://ontario.hibid.com/api/v1/lot/list", "global": "https://hibid.com/api/v1/lot/list"}
PAYLOAD = {"pn": None, "ipp": 100, "isArchive": "false", "filter": "online", "status": "closing"}
HEADERS = {
    "authority": "hibid.com",
    "sec-ch-ua": '"Google Chrome";v="89", "Chromium";v="89", ";Not A Brand";v="99"',
    "x-requested-with": "XMLHttpRequest",
    "sec-ch-ua-mobile": "?0",
    "user-agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/89.0.4389.114 Safari/537.36",
    "accept": "*/*",
    "sec-fetch-site": "same-origin",
    "sec-fetch-mode": "cors",
    "sec-fetch-dest": "empty",
    "referer": "https://hibid.com/lots/?filter=online&status=closing",
    "accept-language": "en-US,en;q=0.9,fr;q=0.8,ro;q=0.7",
}
COOKIES = {"UseInfiniteScroll": "true", "emailcta": "pagehits=3&userdismissed=true"}
STATES = {
    "AL": 1,
    "AK": 2,
    "AS": 3,
    "AZ": 4,
    "AR": 5,
    "CA": 6,
    "CO": 7,
    "CT": 8,
    "DE": 9,
    "DC": 10,
    "FL": 11,
    "GA": 12,
    "GU": 13,
    "HI": 14,
    "ID": 15,
    "IL": 16,
    "IN": 17,
    "IA": 18,
    "KS": 19,
    "KY": 20,
    "LA": 21,
    "ME": 22,
    "MD": 23,
    "MA": 24,
    "MI": 25,
    "MN": 26,
    "MS": 27,
    "MO": 28,
    "MT": 29,
    "NE": 30,
    "NV": 31,
    "NH": 32,
    "NJ": 33,
    "NM": 34,
    "NY": 35,
    "NC": 36,
    "ND": 37,
    "MP": 38,
    "OH": 39,
    "OK": 40,
    "OR": 41,
    "PA": 42,
    "PR": 43,
    "RI": 44,
    "SC": 45,
    "SD": 46,
    "TN": 47,
    "TX": 48,
    "UT": 49,
    "VT": 50,
    "VA": 51,
    "VI": 52,
    "WA": 53,
    "WV": 54,
    "WI": 55,
    "WY": 56,
    "AB": 57,
    "BC": 58,
    "MB": 59,
    "NB": 60,
    "NL": 61,
    "NT": 62,
    "NS": 63,
    "NU": 64,
    "ON": 65,
    "PE": 66,
    "QC": 67,
    "SK": 68,
    "YT": 69,
}
# Site options
GLOBAL = "global"
ONTARIO = "ontario"
