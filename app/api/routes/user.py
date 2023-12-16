from fastapi import APIRouter
from ...models.user import User
from ...database import supabase

from ...utils import convert_to_object

router = APIRouter()

# [GET Routes]
@router.get("/user")
def get_user():
    try:
        res = supabase.table("users").select("*").execute()

        return {"data" : res.data, "error" : "none"}
    except Exception as err:
        return {"data" : [], "error" : err}

# [POST Routes]
@router.post("/user")
def create_user(new_user: User):
    try:
        res = supabase.table("users").insert({
            "email" : new_user.email,
            "total_apps": new_user.total_apps,
            "rejected_apps": new_user.rejected_apps,
            "pending_apps": new_user.pending_apps,
            "accepted_apps": new_user.accepted_apps
        }).execute()

        return {"data" : res.data, "error" : "none"}
    except Exception as err:
        return {"data" : [], "error" : err}

# [PUT Routes]
@router.put("/user/{user_id}")
def update_users(user_id: int, update_user: User):
    try:
        updateJobApp = convert_to_object(update_user)

        res = supabase.table("users").update(updateJobApp).eq("id", user_id).execute()

        return {"data" : res.data, "error" : "none"}
    except Exception as err:
        return {"data" : [], "error" : err}

# [DELETE Routes]
@router.delete("/user/{user_id}")
def delete_user(user_id : int):
    try:
        res = supabase.table("users").delete().eq("id", user_id).execute()

        return {"data" : res.data, "error" : "none"}
    # If an Exception has occured
    except Exception as err:
        return {"data" : [], "error" : err}