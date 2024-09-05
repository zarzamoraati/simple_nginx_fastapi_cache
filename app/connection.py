from pymongo import MongoClient
from fastapi import HTTPException
from  pymongo.database import Database
import os
from dotenv import load_dotenv

load_dotenv()

def retrieve_db() -> Database | HTTPException:
    status=None
    uri=os.getenv("MONGO_URI")
    db_name=os.getenv("DB_NAME")
    if uri == None or uri == "":
        status+="\nThere was a problem reading 'MONGO_URI' environment var"
    if db_name == None  or db_name == "":
        status+="\nThere was a problem reading 'DB_NAME' environment var"
    if status is not None:
        raise HTTPException(status)
    
    client=MongoClient(uri)
    db=client[db_name]
    return db