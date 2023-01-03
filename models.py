from database import Base
from sqlalchemy import Column, Integer, String, DateTime, Boolean, ForeignKey, Date

from sqlalchemy.orm import relationship


class Users(Base):
    __tablename__="user"

    user_id = Column(Integer, primary_key=True, index=True, autoincrement=True)
    nama = Column(String(30))
    email = Column(String(40), unique=True)
    password = Column(String(40))

class Tabungan(Base):
    __tablename__="tabungan"

    user_id = Column(Integer, primary_key=True, index=True)
    uang_gopay = Column(Integer)
    uang_cash = Column(Integer)
    uang_rekening = Column(Integer)
    
