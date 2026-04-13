from fastapi import FastAPI
from database.connection import Base, engine
from routes.user import user_routes

app = FastAPI()

Base.metadata.create_all(bind=engine)

@app.get("/")
def api_start():
    return {"message": "API started 🚀"}

app.include_router(user_routes.router)
