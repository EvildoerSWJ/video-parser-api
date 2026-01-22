import requests

HEADERS = {
    "User-Agent": (
        "Mozilla/5.0 (Windows NT 10.0; Win64; x64) "
        "AppleWebKit/537.36 (KHTML, like Gecko) "
        "Chrome/121.0.0.0 Safari/537.36"
    ),
    "Accept": "application/json, text/plain, */*",
    "Referer": "https://www.douyin.com/",
}

def get(url, **kwargs):
    return requests.get(
        url,
        headers=HEADERS,
        timeout=10,
        allow_redirects=kwargs.pop("allow_redirects", True)
    )
def post(url, **kwargs):
    return requests.get(
        url,
        headers=HEADERS,
        timeout=10,
        allow_redirects=kwargs.pop("allow_redirects", True)
    )
