from pydantic import BaseModel , EmailStr , AnyUrl , Field , field_validator , model_validator , computed_field
from typing import List , Dict , Optional , Annotated 

# class Patient(BaseModel):

#     # By defaults all are requiees
#     name : Annotated[str , Field(max_length= 50 , description="Give me the name of the patient" , examples=['Shantnu' , "Amit"] , title="Name of the patient")]
#     age : int = Field(gt=0 , lt=150)
#     email : EmailStr # to validate email
#     linkedin_url : AnyUrl
#     weight : Annotated[float , Field(strict=True , gt = 0)] 

#     # But can make them optional
#     married : Annotated[bool , Field(default= False , description="Weather the patient is married or not")] 
#     # allergies : List[str]i
#     allergies : Optional[List[str]] = None
#     contact_details : Dict[str , str]

def insert_values(Patient_obj):
    print(Patient_obj.name)
    print(Patient_obj.age)
    print("BMI" , Patient_obj.bmi)
    print(Patient_obj.address.city)
    print(Patient_obj.address.pin)
    print("Object Inserted sucessfully.... ")
    

# p_data = {"name" : "shantnu" , "age" : 30 ,'email' : 'shans@jsis.com', 'linkedin_url' :"https://shan.com/about" , "weight" : 70.34 , "married" : True ,'contact_details' : {"phone" : '29383' , 'emial': "shans@38484ns"} }
#         #    "allergies" : ["sha" , "abc"] ,


# Patient_obj = Patient(**p_data)

# insert_values(Patient_obj)
class Adress(BaseModel):
    city : str
    state : str
    pin : int

class Patient_hdfc(BaseModel):

    name : str
    email : EmailStr
    height : float
    weight : float
    age : int
    married : bool
    allergies : List[List]
    address : Adress            # nested 
    contact_details : Dict[str , str]

    @field_validator('email')
    @classmethod
    def email_validator(cls , value):
        valid_domain = ['hdfc.com' , 'icici.com']

        domain_name = value.split("@")[1]

        if domain_name not in valid_domain:
            raise ValueError("NOT a valid email")

        return value
    
    @field_validator('name') # Mode -> before and after
    @classmethod
    def transform_name(cls ,value ):
        return value.upper()
    
    @field_validator('age' , mode = 'after') # before will not work as 
    @classmethod
    def validate_age_range(cls , value):
        if 0 < value < 100:
            return value
        else:
            raise ValueError("Age needs to be correct")
        
    # Data validation on multiple fields
    @model_validator(mode= "after")
    @classmethod
    def validate_age_emergency_contact(cls , model):
        if model.age > 60 and "emergency" not in model.contact_details:
            raise ValueError("Can't create a patient with age > 60 and no emegency contact")
        else:
            return model

    # Using feilds to calculate some other fields 
    @computed_field
    @property
    def bmi(self)-> float:
        bmi = round((self.weight / self.height**2) , 5)
        return bmi

adress_dict = {'city' : 'Delhi' , 'state' : "Delhi" , 'pin' : '110032'}
adress_obj = Adress(**adress_dict)
p_data_new = {"name" : "shantnu" ,"weight":'89.40' , 'height' : '170.18' , "age" : '65' ,'email' : 'shans@hdfc.com', 'linkedin_url' :"https://shan.com/about" , "weight" : 70.34 , "married" : True ,'allergies':[['sha'] , ['shan']], 'contact_details' : {"phone" : '29383' , 'emial': "shans@38484ns" , 'emergency': 'abc'} , 'address' : adress_obj }
patient_1 = Patient_hdfc(**p_data_new)
a = patient_1.model_dump(mode= 'python' , include=['name'])  
# a = patient_1.model_dump(mode= 'python' , include=['name'] , exclude= ['name'])  
print(a)
insert_values(patient_1)
