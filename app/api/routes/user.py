from fastapi import APIRouter
from ...models.user import User

router = APIRouter()

# [POST Routes]
@router.post("/user")
def create_user(new_user: User):
    return {"data" : "New User Created!"}

# [GET Routes]
@router.get("/user")
def get_user():
    return {"data" : "Current Users"}

# [DELETE Routes]
# @router.delete("/user/{user_id}")
# def delete_job_app(job_id : int):
#     dataStr = "Deleted Job App" + job_id
#     return {"data" : "Deleted Job App"}

# # [PUT Routes]
# @router.put("/user/{user_id}")
# def update_job_app(job_id:int):
#     dataStr = "Updated Job App" + job_id