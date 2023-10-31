from fastapi import APIRouter
from ...models.job_app import JobApp
from ...database import supabase

router = APIRouter()

# [POST Routes]
@router.post("/jobapp")
def create_job_app(new_job_app: JobApp):
    return {"data" : "New Job App Created!"}

# [GET Routes]
@router.get("/jobapp")
def get_job_app():
    job_app_data = supabase.table("job_apps").select("*").execute()
    return {"data" : job_app_data.data}

# [DELETE Routes]
@router.delete("/jobapp/{job_id}")
def delete_job_app(job_id : int):
    dataStr = "Deleted Job App" + job_id
    return {"data" : "Deleted Job App"}

# [PUT Routes]
@router.put("/jobapp/{job_id}")
def update_job_app(job_id:int):
    dataStr = "Updated Job App" + job_id