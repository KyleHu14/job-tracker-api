# Imports
from fastapi import FastAPI, APIRouter
from .routers import job_app


app = FastAPI()

# Note : Order matters! Whichever one matches first is the one

# Include routers
app.include_router(job_app.router)

# Get Method
@app.get("/")
def root():
    return {"message": "Hello World"}