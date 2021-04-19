URL = "https://ontario.hibid.com/api/v1/lot/list"
PAYLOAD = {"pn": None, "ipp": 100, "isArchive": "false", "filter": "biddable", "status": "open"}
HEADERS = {
    "authority": "ontario.hibid.com",
    "sec-ch-ua": '"Google Chrome";v="89", "Chromium";v="89", ";Not A Brand";v="99"',
    "x-requested-with": "XMLHttpRequest",
    "sec-ch-ua-mobile": "?0",
    "user-agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/89.0.4389.114 Safari/537.36",
    "accept": "*/*",
    "sec-fetch-site": "same-origin",
    "sec-fetch-mode": "cors",
    "sec-fetch-dest": "empty",
    "referer": "https://ontario.hibid.com/lots/?filter=biddable",
    "accept-language": "en-US,en;q=0.9,fr;q=0.8,ro;q=0.7",
}
COOKIES = {"UseInfiniteScroll": "true", "emailcta": "pagehits=3&userdismissed=true"}
