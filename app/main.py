# Imports
from fastapi import FastAPI, APIRouter
from .routers import job_app


app = FastAPI()

# Include routers
app.include_router(job_app.router)

# Get Method
@app.get("/")
def root():
    return {"message": "Welcome to the Job App API"}

