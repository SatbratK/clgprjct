from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session
from app.database import get_db
from app.models import Order

router = APIRouter()

@router.post("/orders/")
def place_order(user_id: int, product_id: int, quantity: int, db: Session = Depends(get_db)):
    new_order = Order(user_id=user_id, product_id=product_id, quantity=quantity)
    db.add(new_order)
    db.commit()
    return {"message": "Order placed successfully"}
