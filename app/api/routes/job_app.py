from fastapi import APIRouter
from ...models.job_app import JobApp
from ...database import supabase

router = APIRouter()

# [POST Routes]
@router.post("/jobapp")
def create_job_app(new_job_app: JobApp):
    try:
        # Create a new job app given the new_job_app passed through the request
        res = supabase.table("job_apps").insert({
            "title" : new_job_app.title,
            "company_name" : new_job_app.company_name,
            "location" : new_job_app.location,
            "status" : new_job_app.status,
            "date" : new_job_app.date,
            "user_email" : new_job_app.user_email,
            "link" : new_job_app.link
        }).execute()

        # Return response
        return {"data" : res.data, "error" : "none"}
    except Exception as err:
        return {"data" : [], "error" : err}

# [GET Routes]
@router.get("/jobapp")
def get_job_app():
    try:
        # Get data from supabase
        res = supabase.table("job_apps").select("*").execute()

        # Return Data
        return {"data" : res.data, "error" : "none"}
    # If an Exception has occured
    except Exception as err:
        return {"data" : [], "error" : err}

# [DELETE Routes]
@router.delete("/jobapp/{job_id}")
def delete_job_app(job_id : int):
    dataStr = "Deleted Job App" + job_id
    return {"data" : "Deleted Job App"}

# [PUT Routes]
@router.put("/jobapp/{job_id}")
def update_job_app(job_id:int):
    dataStr = "Updated Job App" + job_id