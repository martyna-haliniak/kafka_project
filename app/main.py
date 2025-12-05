from fastapi import FastAPI
from app.routes.producer_routes import router as producer_router

app = FastAPI()

# Register routes
app.include_router(producer_router)

@app.get("/")
def root():
    return {"message": "API is running"}
