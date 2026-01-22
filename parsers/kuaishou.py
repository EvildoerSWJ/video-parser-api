import re
from utils.http import post

def parse_kuaishou(url):
    photo_id = re.search(r'photo/(\w+)', url).group(1)

    api = "https://www.kuaishou.com/graphql"
    payload = {
        "operationName": "visionVideoDetail",
        "variables": {"photoId": photo_id},
        "query": "query visionVideoDetail($photoId: String) { visionVideoDetail(photoId: $photoId) { photo { videoResource { playUrl }}}}"
    }

    data = post(api, json=payload).json()
    video = data["data"]["visionVideoDetail"]["photo"]["videoResource"]

    return {
        "code": 200,
        "platform": "kuaishou",
        "video": {
            "nwm": video["playUrl"]
        }
    }
