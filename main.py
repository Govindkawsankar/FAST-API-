from fastapi import FastAPI , Path , HTTPException , Query 
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

@app.get("/patient/{patient_id}")
def view_patient(patient_id : str = Path(... , description = "ID of the patient , example P001" )):
   data = load()
   if patient_id in data :
      return data[patient_id]

   return {"error" : "patient id not found "} 

@app.get("/sort")
def sort_patients( sort_by : str = Query(... , description = "sort_by height , weight or bmi " ) 
, order : str = Query("asc", description = "asc or desc")) :
   valid_feilds = ["height" , "weight" , "bmi"] 
   if sort_by not in valid_feilds:
     raise HTTPException(status_code = 400 , detail = f" invalid . select from {valid_feilds}") 

   if order not in ["asc", "desc"] :
      raise HTTPException(status_code = 400 , detail
                           = f" invalid order .  select  from {"asc", "desc"}")

   data = load()
   sort_order = True if order == "desc" else False 
   sort_data = sorted(data.values() , key = lambda x: x.get(sort_by, 0) , reverse = sort_order)
   return sort_data 


