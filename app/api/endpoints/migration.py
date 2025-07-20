import logging
import subprocess
from fastapi import APIRouter
from app.core.responses import response

router = APIRouter(prefix="/migration", tags=["migration"])


@router.get("/migrate-users-db/")
def migrate_users_db():
    try:
        result = subprocess.run(
            ["alembic", "-c", "alembic_users_db/alembic.ini", "upgrade", "head"],
            capture_output=True,
            text=True,
            check=True,
        )
        logging.info(result)
        return response("db is migrated", 200, "success")
    except subprocess.CalledProcessError as e:
        return response("db is not migrated", 500, f"error: {str(e)}")

