from fastapi import FastAPI

app = FastAPI()


# TODO: message가 Hello gangnam을 출력하게 수정
@app.get("/")
async def root():
    return {"message": "Hello bangnam"}