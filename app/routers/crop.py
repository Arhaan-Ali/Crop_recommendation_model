from fastapi import APIRouter, HTTPException
from app.models.crop import CropRecommendRequest, CropRecommendResponse
from app.services.crop_service import recommend_crop_service

router = APIRouter(prefix="/crop", tags=["crop"])

@router.post("/recommend", response_model=CropRecommendResponse)
def recommend_crop(request: CropRecommendRequest):
    try:
        return recommend_crop_service(request)
    except Exception as e:
        raise HTTPException(status_code=400, detail=str(e))
