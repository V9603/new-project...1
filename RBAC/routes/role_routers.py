from fastapi import APIRouter
from database import conn, cursor
from permission_guard import authorize

router = APIRouter()

@router.post("/create-role")

def create_role(user_id:int, role_name:str):

    authorize(user_id,"CREATE_ROLE")

    query = """
    INSERT INTO roles(tenant_id,name)
    VALUES (%s,%s)
    """

    cursor.execute(query,(1,role_name))
    conn.commit()

    return {"message":"Role created sucessfully"}
@router.post("/assign-role")

def assign_role(user_id:int,target_user:int,role_id:int):

    authorize(user_id,"ASSIGN_ROLE")

    query="""
    INSERT INTO user_roles(user_id,role_id)
    VALUES (?,?)
    """

    cursor.execute(query,(target_user,role_id))
    conn.commit()

    return {"message":"Role assigned"}
@router.delete("/revoke-role")

def revoke_role(user_id:int,target_user:int,role_id:int):

    authorize(user_id,"REVOKE_ROLE")

    query="""
    DELETE FROM user_roles
    WHERE user_id=? AND role_id=?
    """

    cursor.execute(query,(target_user,role_id))
    conn.commit()

    return {"message":"Role revoked"}
@router.post("/add-marks")

def add_marks(user_id:int):

    authorize(user_id,"ADD_MARKS")

    return {"message":"Marks added"}
from fastapi import HTTPException
from permission_helper import check_permission

def authorize(user_id, permission):

    allowed = check_permission(user_id, permission)

    if not allowed:
        raise HTTPException(
            status_code=403,
            detail="Access Denied"
        )
from fastapi import APIRouter

router = APIRouter()

@router.get("/test")
def test():
    return {"message": "Router working"}

@router.post("/create-role")
def create_role(user_id:int, role_name:str):

    authorize(user_id,"CREATE_ROLE")

    query = """
    INSERT INTO roles(tenant_id, name)
    VALUES (%s,%s)
    """

    cursor.execute(query,(1,role_name))
    conn.commit()

    return {"message":"Role created sucessfully"}

# implement assign role api a user
@router.post("/assign-role")
def assign_role(user_id: int, target_user: int, role_id: int):

    authorize(user_id, "ASSIGN_ROLE")

    query = """
    INSERT IGNORE INTO user_roles(user_id, role_id)
    VALUES (%s, %s)
    """

    cursor.execute(query, (target_user, role_id))
    conn.commit()

    return {"message": "Role assigned successfully"}

# user roles assignrole function;
@router.get("/user-roles/{user_id}")
def get_user_roles(user_id: int):

    query = """
    SELECT r.name
    FROM user_roles ur
    JOIN roles r ON ur.role_id = r.id
    WHERE ur.user_id = %s
    """

    cursor.execute(query, (user_id,))
    roles = cursor.fetchall()

    return {"roles": roles}

@router.get("/user-permissions/{user_id}")
def get_user_permissions(user_id: int):

    query = """
    SELECT p.name
    FROM user_roles ur
    JOIN role_permissions rp ON ur.role_id = rp.role_id
    JOIN permissions p ON rp.permission_id = p.id
    WHERE ur.user_id = %s
    """

    cursor.execute(query, (user_id,))
    permissions = cursor.fetchall()

    return {"permissions": permissions}

