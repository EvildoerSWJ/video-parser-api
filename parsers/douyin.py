import requests

# 这里用示例第三方 API
# 注意：真实环境请替换成可用的接口，有些 API 需要注册或者带 token
API_URL = "https://apis.jxcxin.cn/api/douyin?url="

def parse_douyin(url):
    """
    调用第三方 API 解析抖音视频/笔记
    """
    try:
        resp = requests.get(API_URL + url, timeout=10)
        if resp.status_code != 200:
            return {"code": 500, "msg": f"第三方接口请求失败：{resp.status_code}"}
        data = resp.json()

        # 返回示例格式，适配你的 FastAPI 接口
        return data

    except requests.exceptions.RequestException as e:
        return {"code": 500, "msg": str(e)}
    except Exception as e:
        return {"code": 500, "msg": str(e)}
