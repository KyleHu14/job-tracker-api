from fastapi import APIRouter
from ..models import JobApp

router = APIRouter()

@router.post("/jobapp")
def create_job_app(new_job_app: JobApp):
    print(new_job_app)
    return {"data" : "new posat"}