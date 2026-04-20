from fastapi import FastAPI
from database.connection import Base, engine
from routes.user.user_routes import router as user_routes
from routes.product.product_routes import router as product_routes
from routes.auth.auth_routes import router as auth_routes

app = FastAPI()

Base.metadata.create_all(bind=engine)

@app.get("/")
def api_start():
    return {"message": "API started 🚀"}

app.include_router(user_routes)
app.include_router(product_routes)
app.include_router(auth_routes)
