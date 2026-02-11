from fastapi import FastAPI
from app.routers import crop, fertilizer, soil

app = FastAPI()
  
app.include_router(crop.router)
app.include_router(fertilizer.router)
app.include_router(soil.router)

@app.get("/")
def root():
    return {"message": "Crop Recommendation API"}
