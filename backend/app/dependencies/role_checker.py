from fastapi import HTTPException

def require_manager(user):
    if user["role"] != "manager":
        raise HTTPException(status_code=403, detail="Manager access required")