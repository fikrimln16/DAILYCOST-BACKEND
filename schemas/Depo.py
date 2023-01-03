from pydantic import BaseModel

class Depo(BaseModel):
    user_id:int
    uang_gopay:int
    uang_cash:int
    uang_rekening:int
    
    class Config:
        orm_mode=True