from fastapi import FastAPI
from database import Base, SessionLocal, engine
from fastapi.middleware.cors import CORSMiddleware
from router import user

import uvicorn

Base.metadata.create_all(bind=engine)


app = FastAPI()

origins = ["*"]

app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=['*'],
    allow_headers=['*'],
)

def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()

app.include_router(user.router)

