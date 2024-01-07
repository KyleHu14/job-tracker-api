from fastapi import APIRouter
from ...models.job_app import JobApp
from ...database import supabase

router = APIRouter()

def convert_to_object(inputClass):
    '''
    Converts a pydantic class into a dictionary. 
    '''
    finalObj = {}

    for row in inputClass:
        if row[1]:
            finalObj[row[0]] = row[1]
        
    return finalObj

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

        # Increment total apps
        incrementRes = supabase.rpc("increment_total_apps", params={"useremail" : new_job_app.user_email}).execute()
        incrementStatusRes = supabase.rpc(f"increment_{new_job_app.status}_apps", params={"useremail" : new_job_app.user_email}).execute()

        # Return response
        return {"data" : res.data, "error" : "none"}
    except Exception as err:
        return {"data" : [], "error" : err}

# [PUT Routes]
@router.put("/jobapp/{job_id}")
def update_job_app(job_id:int, update_job_app: JobApp):
    # update_job_app takes on the form as an array of tuples
    # Here is an example : 
    # ('title', 'API title')
    # ('company_name', '')
    # ('location', '')
    # ('status', '')
    # ('date', 'API title')
    # ('user_email', 'lloydpearce4@gmail.com')
    # ('link', 'API title')
    # Row represents one of these tuples
    try:
        # We convert the update_job_app into an object since .update() takes in an object
        updateObj = convert_to_object(update_job_app)

        res = supabase.table("job_apps").update(updateObj).eq("id", job_id).execute()

        return {"data" : res.data, "error" : "none"} 
    except Exception as err:
        return {"data" : [], "error" : err}

# [DELETE Routes]
@router.delete("/jobapp/{job_id}")
def delete_job_app(job_id : int):
    try:
        res = supabase.table("job_apps").delete().eq("id", job_id).execute()

        # Decrement total apps
        decrementRes = supabase.rpc("decrement_total_apps", params={"useremail" : res.data[0]["user_email"]}).execute()
        decrementStatusRes = supabase.rpc(f"decrement_{res.data[0]["status"]}_apps", params={"useremail" : res.data[0]["user_email"]}).execute()

        return {"data" : res.data, "error" : "none"}
    # If an Exception has occured
    except Exception as err:
        return {"data" : [], "error" : err}