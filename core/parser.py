from core.detector import detect_platform
from parsers.douyin import parse_douyin
# from parsers.tiktok import parse_tiktok
# from parsers.kuaishou import parse_kuaishou
# from parsers.xhs import parse_xhs

def parse(url: str):
    platform = detect_platform(url)

    if platform == "douyin":
        return parse_douyin(url)
    # if platform == "tiktok":
    #     return parse_tiktok(url)
    # if platform == "kuaishou":
    #     return parse_kuaishou(url)
    # if platform == "xhs":
    #     return parse_xhs(url)

    return {"code": 400, "msg": "Unsupported platform"}
