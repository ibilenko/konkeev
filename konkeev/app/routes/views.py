from fastapi import APIRouter, HTTPException

from connection.db_connector import DatabaseConnector

router = APIRouter()

@router.post("/get_table")
async def proc(table_name: str):
    db_conn = DatabaseConnector()
    records = db_conn.select_table(table_name)
    if records:
        return {'value': records}
    else:
        raise HTTPException(status_code=404, detail='No such table')