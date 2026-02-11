from fastapi import APIRouter, HTTPException
from app.models.fertilizer import (
    FertilizerLogicRequest, FertilizerLogicResponse,
    FertilizerNeuralRequest, FertilizerNeuralResponse
)
from app.services.fertilizer_service import (
    fertilizer_logic_service, fertilizer_neural_service
)

router = APIRouter(prefix="/fertilizer", tags=["fertilizer"])

@router.post("/logic", response_model=FertilizerLogicResponse)
def fertilizer_logic(request: FertilizerLogicRequest):
    try:
        return fertilizer_logic_service(request)
    except Exception as e:
        raise HTTPException(status_code=400, detail=str(e))

@router.post("/neural", response_model=FertilizerNeuralResponse)
def fertilizer_neural(request: FertilizerNeuralRequest):
    try:
        return fertilizer_neural_service(request)
    except Exception as e:
        raise HTTPException(status_code=400, detail=str(e))
