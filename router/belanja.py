from fastapi import Depends, APIRouter, HTTPException, status
from database import SessionLocal
from schemas.Belanja import Belanja
from sqlalchemy.orm import Session
from typing import List
from schemas.User import UserSchema
from schemas.UserLogin import UserLogin
from schemas.Depo import Depo
from schemas.Email import Email
from datetime import datetime
# from pytz import timezone
from models import Users


router = APIRouter()

def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()

@router.post("/belanja", tags=["pengeluaran"])
async def get_total_users(belanja:Belanja, db:Session=Depends(get_db)):
    query = "INSERT INTO pengeluaran VALUES(null, '%s', '%s', %d, '%s', %d)"%(belanja.nama, belanja.tanggal, belanja.jumlah, belanja.pembayaran, belanja.user_id)
    try:
        db.execute(query)
        db.commit()
        db.close()
        getUang = db.execute("SELECT uang_gopay, uang_cash, uang_rekening FROM tabungan WHERE user_id = %d"%belanja.user_id).fetchall()
        for hasil in getUang:
            uang_gopay = hasil[0]
            uang_cash = hasil[1]
            uang_rekening = hasil[2]
            if belanja.pembayaran == 'GOPAY':
                uang_gopay_update = uang_gopay - belanja.jumlah
                db.execute("UPDATE tabungan SET uang_cash = %d WHERE user_id = %d"%(uang_gopay_update, belanja.user_id))
                db.commit()
            elif belanja.pembayaran == 'REKENING':
                uang_rekening_update = uang_rekening - belanja.jumlah
                db.execute("UPDATE tabungan SET uang_rekening = %d WHERE user_id = %d"%(uang_rekening_update, belanja.user_id))
                db.commit()
            elif belanja.pembayaran == 'CASH':
                uang_cash_update = uang_cash - belanja.jumlah
                db.execute("UPDATE tabungan SET uang_cash = %d WHERE user_id = %d"%(uang_cash_update, belanja.user_id))
                db.commit()
            return {"msg" : "berhasil"}
    except:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND) 

