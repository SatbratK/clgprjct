from fastapi import FastAPI
from app.routes import auth, products, orders

app = FastAPI()

app.include_router(auth.router, prefix="/auth")
app.include_router(products.router, prefix="/products")
app.include_router(orders.router, prefix="/orders")

@app.get("/")
def home():
    return {"message": "Voice Powered Shopping Bot API is running"}
