
from app.models.soil import SoilTypeRequest, SoilTypeResponse

def soil_type_service(request: SoilTypeRequest) -> SoilTypeResponse:
    # Dummy response for testing
    return SoilTypeResponse(soil_type="clay", probabilities={"clay": 0.7, "sandy": 0.3})
