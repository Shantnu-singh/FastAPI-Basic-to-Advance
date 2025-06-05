from pydantic import BaseModel , EmailStr , AnyUrl , Field 
from typing import List , Dict , Optional , Annotated

class Patient(BaseModel):

    # By defaults all are requiees
    name : Annotated[str , Field(max_length= 50 , description="Give me the name of the patient" , examples=['Shantnu' , "Amit"] , title="Name of the patient")]
    age : int = Field(gt=0 , lt=150)
    email : EmailStr # to validate email
    linkedin_url : AnyUrl
    weight : Annotated[float , Field(strict=True , gt = 0)] 

    # But can make them optional
    married : Annotated[bool , Field(default= False , description="Weather the patient is married or not")] 
    # allergies : List[str]
    allergies : Optional[List[str]] = None
    contact_details : Dict[str , str]

def insert_values(Patient_obj):
    print(Patient_obj.name)
    print(Patient_obj.age)
    print("Object Inserted sucessfully.... ")

p_data = {"name" : "shantnu" , "age" : 30 ,'email' : 'shans@jsis.com', 'linkedin_url' :"https://shan.com/about" , "weight" : 70.34 , "married" : True ,'contact_details' : {"phone" : '29383' , 'emial': "shans@38484ns"} }
        #    "allergies" : ["sha" , "abc"] ,


Patient_obj = Patient(**p_data)

insert_values(Patient_obj)


