from fastapi import FastAPI , Path , HTTPException
import json

app = FastAPI()

def get_data():
    with open("patient.json", "r") as file:
        data = json.load(file)
    return data
    

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