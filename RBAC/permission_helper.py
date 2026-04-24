from database import cursor

def check_permission(user_id, permission):

    query = """
    SELECT p.name
    FROM user_roles ur
    JOIN role_permissions rp ON ur.role_id = rp.role_id
    JOIN permissions p ON rp.permission_id = p.id
    WHERE ur.user_id = %s
    AND p.name = %s
    """

    cursor.execute(query, (user_id, permission))

    result = cursor.fetchone()

    if result:
        return True
    else:
        return False