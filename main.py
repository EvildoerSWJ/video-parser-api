# from fastapi import FastAPI, Query
# from core.parser import parse

# app = FastAPI(title="Multi Video Parser API")

# @app.get("/api/parse")
# def api_parse(url: str = Query(..., description="视频分享链接")):
#     return parse(url)


from fastapi import FastAPI, Query
from parsers.douyin import parse_douyin
from parsers.kuaishou import parse_kuaishou

app = FastAPI()

@app.get("/api/parse")
def api_parse(url: str = Query(..., description="抖音短链接或长链接")):
    return parse_douyin(url)
@app.get('/api/throttle')
def api_parse(url: str = Query(..., description="快手短链接或长链接")):
    return parse_kuaishou(url)

