from pydantic import BaseModel

class UserSchema(BaseModel):
    nama:str
    email:str
    password:str
    
    class Config:
        orm_mode=True
