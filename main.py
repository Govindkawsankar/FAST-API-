from fastapi import FastAPI 
import json 

app = FastAPI()
@app.get("/")
def hello():
    return{"message" : "Patients management system API"}
def load():
    with open("patients.json" , "r") as f :
     data = json.load(f)
     return data
    
@app.get("/view")
def view():
   data = load()
   return data 