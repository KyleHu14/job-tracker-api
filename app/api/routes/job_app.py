from fastapi import APIRouter
from ...models.job_app import JobApp

router = APIRouter()

# [POST Routes]
@router.post("/jobapp")
def create_job_app(new_job_app: JobApp):
    return {"data" : "New Job App!"}

# [GET Routes]
@router.get("/jobapp")
def get_job_app():
    return {"data" : "Current Job Apps"}

# [DELETE Routes]
@router.delete("/jobapp/{job_id}")
def delete_job_app(job_id : int):
    dataStr = "Deleted Job App" + job_id
    return {"data" : "Deleted Job App"}