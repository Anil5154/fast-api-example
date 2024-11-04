from fastapi import FastAPI

app = FastAPI()


@app.get("/dev/hello")
async def root():
    return {"message": "Hello World from server 1"}