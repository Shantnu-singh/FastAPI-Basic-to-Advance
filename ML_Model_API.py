from fastapi import FastAPI , HTTPException 
from fastapi.responses import JSONResponse
import pickle
from pydantic import BaseModel , Field , computed_field 
from typing import Literal
import pandas as pd

app = FastAPI()

@app.get("/health_")
def health_cond():
    try:
        return JSONResponse(content= {"Message : This application is working fine"} , status_code= 200)
    except:
        raise HTTPException(status_code= 400 , detail="App is not working fine")
    
def get_model():
    with open("model.pkl" , "rb") as f:
        model = pickle.load(f)
    return model

tier_1_cities = ["Mumbai", "Delhi", "Bangalore", "Chennai", "Kolkata", "Hyderabad", "Pune"]
tier_2_cities = [
    "Jaipur", "Chandigarh", "Indore", "Lucknow", "Patna", "Ranchi", "Visakhapatnam", "Coimbatore",
    "Bhopal", "Nagpur", "Vadodara", "Surat", "Rajkot", "Jodhpur", "Raipur", "Amritsar", "Varanasi",
    "Agra", "Dehradun", "Mysore", "Jabalpur", "Guwahati", "Thiruvananthapuram", "Ludhiana", "Nashik",
    "Allahabad", "Udaipur", "Aurangabad", "Hubli", "Belgaum", "Salem", "Vijayawada", "Tiruchirappalli",
    "Bhavnagar", "Gwalior", "Dhanbad", "Bareilly", "Aligarh", "Gaya", "Kozhikode", "Warangal",
    "Kolhapur", "Bilaspur", "Jalandhar", "Noida", "Guntur", "Asansol", "Siliguri"
]


class Customer(BaseModel):
    age :int =  Field(gt = 0 , lt = 150)
    weight :float =  Field(gt = 0 , lt = 200)
    height :float =  Field(gt = 0 , lt = 3)
    income_lpa :float
    smoker : bool
    city : str
    occupation : Literal['retired', 'freelancer', 'student', 'government_job','business_owner', 'unemployed', 'private_job']

    @computed_field
    @property
    def bmi(self)->float:
        return (self.weight / ((self.height)**2))
    
    @computed_field
    @property
    def age_group(self)->str:
        if self.age < 25:
            return "young"
        elif self.age < 45:
            return "Adult"
        elif self.age < 60:
            return "middle_aged"
        else:
            return "senior_citizen"
    @computed_field
    @property
    def city_tier(self)->int:
        if self.city in tier_1_cities:
            return 1
        elif self.city in tier_2_cities:
            return 2
        else:
            return 3
        
    @computed_field
    @property
    def lifestyle_risk(self)->str:
        if self.smoker and self.bmi > 30:
            return "high"
        elif self.smoker and self.bmi > 27:
            return "medium"
        else:
            return "low"

@app.post("/predict")
def predict(customer : Customer):
    try:
        data = pd.DataFrame([{
            "BMI" : customer.bmi,
            "age_category" : customer.age_group,
            'occupation' : customer.occupation,
            "lifestyle" : customer.lifestyle_risk,
            "city_tier" : customer.city_tier,
            "income_lpa" : customer.income_lpa
        }])

        pipeline = get_model()
        y_pred = pipeline.predict(data)

        return JSONResponse(status_code= 200 , content= {"y_pred" : y_pred[0]})
    except:
        raise HTTPException(status_code= 400 , detail={"Something went wrong"})
    



