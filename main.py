from fastapi import FastAPI

app = FastAPI()


@app.get("/qa/hello")
async def root():
    return {"message": "Hello World from server 2"}