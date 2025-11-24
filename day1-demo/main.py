import requests
from fastapi import FastAPI

# 创建API实例
app = FastAPI()

@app.get("/")
async def root():
    return {"message": "Hello World"}


@app.get("/predict")
def predict(text: str):
    return "输入的文本是"+text




requests.request(Po)