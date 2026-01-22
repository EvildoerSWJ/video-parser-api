import re
from utils.http import get

def parse_tiktok(url):
    html = get(url).text
    item_id = re.search(r'"itemId":"(\d+)"', html).group(1)

    api = f"https://www.tiktok.com/api/item/detail/?itemId={item_id}"
    data = get(api).json()

    video = data["itemInfo"]["itemStruct"]["video"]

    return {
        "code": 200,
        "platform": "tiktok",
        "video": {
            "wm": video["downloadAddr"],
            "nwm": video["playAddr"]
        }
    }
