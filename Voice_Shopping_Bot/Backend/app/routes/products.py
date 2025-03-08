from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session
from app.database import get_db
from app.models import Product

router = APIRouter()

@router.get("/products/")
def get_products(db: Session = Depends(get_db)):
    return db.query(Product).all()

@router.post("/products/")
def add_product(name: str, price: float, description: str, db: Session = Depends(get_db)):
    new_product = Product(name=name, price=price, description=description)
    db.add(new_product)
    db.commit()
    return {"message": "Product added"}
