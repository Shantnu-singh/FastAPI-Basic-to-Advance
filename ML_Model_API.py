from fastapi import FastAPI , HTTPException 
from fastapi.responses import JSONResponse

app = FastAPI()

@app.get("/health_")
def health_cond():
    try:
        return JSONResponse(content= {"Message : This application is working fine"} , status_code= 200)
    except:
        raise HTTPException(status_code= 400 , detail="App is not working fine")
    

