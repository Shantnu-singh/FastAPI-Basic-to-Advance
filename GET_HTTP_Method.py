from fastapi import FastAPI
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