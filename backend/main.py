from fastapi import FastAPI, Depends
from fastapi.middleware.cors import CORSMiddleware
from sqlalchemy.orm import Session
from database import Base, engine, get_db
import models

app = FastAPI()

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_methods=["*"],
    allow_headers=["*"],
)

Base.metadata.create_all(bind=engine)

@app.get("/accounts")
def get_accounts(db: Session = Depends(get_db)):
    return db.query(models.Account).all()

@app.get("/accounts/{account_id}")
def get_account(account_id: int, db: Session = Depends(get_db)):
    return db.query(models.Account).filter(models.Account.id == account_id).first()

@app.get("/accounts/segment/{segment}")
def get_by_segment(segment: str, db: Session = Depends(get_db)):
    return db.query(models.Account).filter(models.Account.segment == segment).all()

