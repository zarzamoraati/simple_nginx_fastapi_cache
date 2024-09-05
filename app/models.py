from pydantic import BaseModel
from pydantic import field_validator, Field 
from typing import Optional, List , Union, Dict
from datetime import datetime
from uuid import uuid4
from fastapi import HTTPException

class Contact(BaseModel):
    id:Optional[str]=Field(default_factory=lambda : str(uuid4()))
    date:Optional[datetime]=Field(default_factory= lambda : datetime.today())
    name:str
    phone:str

@field_validator("name")
def check_name(name:str):
    if not isinstance(name, str) or name == "":
        raise HTTPException(status_code=400,detail="Field 'name' is not valid")
    
    