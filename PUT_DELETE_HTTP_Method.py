from fastapi import FastAPI , Path , HTTPException , Query
from pydantic import BaseModel , computed_field , Field
from typing import Annotated , Literal , Optional
from fastapi.responses import JSONResponse

import json  
import os

# Create on more pydentic model


app = FastAPI()

class Patient(BaseModel):
    id : str
    name: str
    city: str
    age: Annotated[int , Field(gt = 0 , lt = 100 , description= 'Age of the patient')]
    gender: Annotated[Literal['male' , 'female' , 'others'] , Field(... , description= 'Details about patient gender')]
    height: float
    weight: float

    @computed_field
    @property
    def bmi(self)->float:
        bmi = round((self.weight / self.height**2) , 5)
        return bmi

    @computed_field
    @property
    def verdict(self)->str:
        if self.bmi < 18.5:
            return "Underweight"
        elif 18.5 <= self.bmi < 24.9:
            return "Normal weight"
        elif 25 <= self.bmi < 29.9:
            return "Overweight" 
        else:
            return "Obese"
        
class Patient_update(BaseModel):
    name: Optional[str] = Field(default=None)
    city: Optional[str] = Field(default=None)
    age: Optional[Annotated[int, Field(gt=0, lt=100)]] = Field(default=None)
    gender: Optional[Literal['male', 'female', 'others']] = Field(default=None)
    height: Optional[float] = Field(default=None)
    weight: Optional[float] = Field(default=None)
         
def get_data():
    with open("Data/patient.json", "r") as file:
        data = json.load(file)
    return data

DATA_FILE = os.path.join(os.path.dirname(__file__), "Data", "patient.json")
def save_data(data):
    with open(DATA_FILE, "w") as file:
        json.dump(data , file)

@app.put("/edit/{patient_id}")
def patient_edit(patient_id : str , patient_data_update :Patient_update):
    all_data = get_data()

    if patient_id not in all_data:
        raise HTTPException(status_code= 400 , detail="Patient id not exist in db")
    
    patient_data = all_data[patient_id]
    patient_data_update = patient_data_update.model_dump(exclude_unset= True)

    for k , v in patient_data_update.items():
      patient_data[k] = v  

    patient_data["id"] = patient_id
    p_obj = Patient(**patient_data)
    patient_data = p_obj.model_dump(exclude= {'id'})

    all_data[patient_id] = patient_data
    print(all_data)

    save_data(all_data)

    return JSONResponse(status_code= 200 , content={"message" : "updation of data is sucessfull"})

@app.delete("/delete/{patient_id}")
def delete_patient(patient_id):
    all_data  = get_data()
    if patient_id not in all_data:
        raise HTTPException(status_code= 400 , detail="Patient id not exist in db")
    
    filter_data = {k:v for k , v in all_data.items() if k != patient_id}
    save_data(filter_data)

    return JSONResponse(status_code= 200 , content={"message" : "Deletion of data is sucessfull"})


@app.post('/create')
def create_patient(patient_data : Patient):
    exist_data = get_data()

    # check if alreay exist
    if patient_data.id in exist_data:
        raise HTTPException(status_code=400, detail="Patient already exists in the data")


    # if new then add in DB
    data = patient_data.model_dump(exclude=['id'])
    exist_data[patient_data.id] = data

    # save as json file
    save_data(exist_data)

    return JSONResponse(status_code= 201 , content= {"message" : "patient created sucessfully"})
    

@app.get("/")
def welcome_msg():
    return {"message": "Welcome to the FastAPI application!"}

@app.get("/about")
def about():
    return {"message": "This is a simple FastAPI application."}

@app.get("/view")
def view():
    try:
        return get_data()  
    except FileNotFoundError:
        return {"error": "File not found. Please ensure 'patient.json' exists."}
    
@app.get("/patient/{patient_id}")
def get_patient(patient_id: str = Path(... , description="The ID of the patient to retrieve" , example= 'P001')):
    # load all data
    data = get_data()
    
    if patient_id in data:
        return data[patient_id]
    else:
        raise HTTPException(status_code=404, detail="Patient not found")
    

@app.get("/sort")
def sort_patient(sort_by : str = Query(... , description= "Sort On the basis od Weight, BMI and height" , example= "bmi"),
                  order :str =  Query("asc" , description= "either in asc or in desc order" , examples= ['asc' , 'desc'])):
    
    acceptable_sort_by = ['bmi' , 'height' , 'weight']

    if sort_by not in acceptable_sort_by:
        return HTTPException(status_code= 400 , detail= "value provided is not right")
    
    try:
        all_data = get_data()
        
        is_desc = True
        if order == "asc":
            is_desc = False 

        ans = []
        for data in all_data.items():
            ans.append((data[1][sort_by] , data[1]))

        ans = sorted(ans , key= lambda x : x[0] , reverse= is_desc)

        return {"sorted_patient" : [i[1] for i in ans]}
    
    except :
        raise HTTPException(status_code= 500 , detail= "Something wrong with the system")



