from fastapi import FastAPI, Request

app = FastAPI()

@app.middleware("http")
async def add_flexibility(request: Request, call_next):
    response = await call_next(request)
    # Add any cross-cutting concerns here (e.g., logging)
    return response
