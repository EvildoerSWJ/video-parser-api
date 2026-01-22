安装python3.11
pip install fastapi uvicorn requests --安装依赖
uvicorn main:app --port 8080 --运行
http://localhost:8080/api/parse?url=https://v.douyin.com/短链接/ --测试
http://localhost:8080/docs --swagger可视化界面



