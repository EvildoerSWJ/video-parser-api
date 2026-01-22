import re
from utils.http import get

def parse_xhs(url):
    note_id = re.search(r'/explore/(\w+)', url).group(1)
    api = f"https://edith.xiaohongshu.com/api/sns/v1/note/{note_id}"

    data = get(api).json()["data"]["note"]
    images = [i["url"] for i in data.get("imageList", [])]

    return {
        "code": 200,
        "platform": "xhs",
        "type": data["type"],
        "images": images,
        "video": data.get("video", {})
    }
