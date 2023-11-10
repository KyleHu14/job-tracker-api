# Fast API
from fastapi import FastAPI, APIRouter

# Routers
from .api.routes import job_app
from .api.routes import user

# Import Metadata / Tags (extra documentation)
from .tags import tags_metadata

app = FastAPI(openapi_tags=tags_metadata)

# Include routers
app.include_router(job_app.router)
app.include_router(user.router)

# Get Method
@app.get("/")
def root():
    return {"message": "Welcome to the Job App API"}