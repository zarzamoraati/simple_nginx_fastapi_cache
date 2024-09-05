from connection import retrieve_db
from bson import ObjectId
from models import Contact
from fastapi import HTTPException


def getAllContacts():
    
   try:
        db=retrieve_db()
        contacts=list(db["contact_collection"].find({}))
        size=len(contacts)
        print(size)
        if  size == 0:
            return []
        contacts_norm=[]
        for contact in contacts:
            contact["_id"]=str(contact["_id"])
            contacts_norm.append(contact)
        return contacts_norm
   except Exception as e:
       return {"error:":e}
       

def getOneContact(id:str):
    try:
        obj_id=ObjectId(id)
        db=retrieve_db()
        response=db["contact_collection"].find_one({"_id":obj_id})
        if response is None:
            raise HTTPException(status_code=404,detail=f"Contact with id:{id}, wasn't found in the collection")
        response["_id"]=str(response["_id"])
        return response
    except Exception as e:
        return {"error":e}
    

def createNewContact(contact:Contact):
    try:
        dict_contact=contact.model_dump()
        db=retrieve_db()
        response=db["contact_collection"].insert_one(dict_contact)
        if not response.inserted_id:
            raise HTTPException(status_code=505,detail="There was a problem written the contact in the collection")
        return {"id":str(response.inserted_id)}
    except Exception as e:
        return {"error":e}
 