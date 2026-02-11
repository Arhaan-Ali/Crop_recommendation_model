from fastapi import APIRouter, HTTPException
from app.models.soil import SoilTypeRequest, SoilTypeResponse
from app.services.soil_service import soil_type_service

router = APIRouter(prefix="/soil", tags=["soil"])

@router.post("/type", response_model=SoilTypeResponse)
def soil_type(request: SoilTypeRequest):
    try:
        return soil_type_service(request)
    except Exception as e:
        raise HTTPException(status_code=400, detail=str(e))
