from pydantic import BaseModel

class Belanja(BaseModel):
    user_id:int
    nama: str
    tanggal:str
    jumlah: int
    pembayaran:str
    
    class Config:
        orm_mode=True