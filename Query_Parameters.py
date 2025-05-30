from fastapi import FastAPI , Path , HTTPException , Query

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



