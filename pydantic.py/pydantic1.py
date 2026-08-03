from pydantic import BaseModel , AnyUrl , Field , EmailStr , field_validator
from typing import List , Dict , Optional , Annotated

class Patient(BaseModel):
    name: Annotated[str , Field(max_length= 50 , title="add the patient name",discription = "write the name " \
    "name of patient in less than 50 chars", example = ["harish", "nitish"] )]
    email: EmailStr
    Linkdin_url: AnyUrl
    age:int = Field(gt = 0 ,lt = 100 ) 
    weight: int = Field(gt=0)
    married: bool
    allergies:Annotated[Optional[List[str]], Field(max_length=5 , Default = "none") ]

    @field_validator("email")
    @classmethod 
    def email_valiadator(cls , value):
       
      valid_domain = ["hdfc.com" ,"icici.com"]

      domain = value.split("@")[-1] 
      if domain not in valid_domain :
       raise ValueError( "email not found ")
    
      return value 

    @field_validator("name")
    @classmethod
    def transform_name(cls , value ):
       return  value.upper()
   
    

       





def insert_patients_data(patient: Patient):
    print(patient.name)
    print(patient.age)
    print(patient.weight)
    print("updated")
    






patient_info = {"name":"govind","email":"abcd@hdfc.com","Linkdin_url":"https://Linkdin.com/1212" ,
                  "age": 18, "weight": 50 , "married":False , "allergies":["dust","no"],
                "contact_details":{"email":"abs@gmail.com", "phone":"7507525087"}}

patient1 =Patient(**patient_info)
insert_patients_data(patient1)

