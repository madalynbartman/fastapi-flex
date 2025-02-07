from fastapi import FastAPI

app = FastAPI()

@app.get("/optimized-endpoint")
async def optimized_endpoint():
    # Use asynchronous processing here
    return {"message": "This endpoint is optimized for performance!"}
