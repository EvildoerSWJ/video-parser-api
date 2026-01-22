def detect_platform(url: str) -> str:
    if "douyin.com" in url:
        return "douyin"
    if "tiktok.com" in url:
        return "tiktok"
    if "kuaishou.com" in url:
        return "kuaishou"
    if "xiaohongshu.com" in url or "xhslink.com" in url:
        return "xhs"
    return "unknown"

