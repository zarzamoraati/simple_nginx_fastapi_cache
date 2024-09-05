from fastapi import FastAPI
import crud
from models import Contact


app=FastAPI()


@app.get("/contacts")
def getAllContacts():
    return crud.getAllContacts()

@app.get("/contacts/{id}")
def getOneContact(id:str):
    return crud.getOneContact(id)

@app.post("/contacts")
def createContact(contact:Contact):
    return crud.createNewContact(contact=contact)