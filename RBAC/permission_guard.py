
from fastapi import HTTPException
from permission_helper import check_permission

def authorize(user_id, permission):

    if not check_permission(user_id, permission):
        raise HTTPException(status_code=403, detail="Access Denied")