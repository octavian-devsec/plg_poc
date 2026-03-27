from fastapi import FastAPI, Request

app: FastAPI = FastAPI()

@app.get("/")
def root(request: Request) -> dict:
    """Root endpoint."""
    result: dict = {
        "message": "Hello, World!"
    }
    return result
