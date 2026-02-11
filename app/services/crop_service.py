from app.models.crop import CropRecommendRequest, CropRecommendResponse

def recommend_crop_service(request: CropRecommendRequest) -> CropRecommendResponse:
    # Dummy response for testing
    return CropRecommendResponse(crop="rice", probabilities={"rice": 0.9, "wheat": 0.1})
