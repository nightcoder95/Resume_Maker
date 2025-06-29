from fastapi import FastAPI

app = FastAPI(
    title="Resume Maker",
    description="This service handles storing and retrieving user resume data.",
    version="1.0.0"
)

@app.get("/", tags=["Root"])
async def read_root():
    """
    A simple root endpoint to confirm the API is running.

    """
    # FastAPI will automatically convert this Python dictionary into a JSON response.
    return {"message": "Welcome to the Resume User-Data Service!"}