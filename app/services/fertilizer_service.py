
from app.models.fertilizer import (
    FertilizerLogicRequest, FertilizerLogicResponse,
    FertilizerNeuralRequest, FertilizerNeuralResponse
)

def fertilizer_logic_service(request: FertilizerLogicRequest) -> FertilizerLogicResponse:
    # Dummy response for testing
    return FertilizerLogicResponse(recommendation={"fertilizer": "NPK", "details": "General purpose"})

def fertilizer_neural_service(request: FertilizerNeuralRequest) -> FertilizerNeuralResponse:
    # Dummy response for testing
    return FertilizerNeuralResponse(fertilizer="Urea", probabilities={"Urea": 0.8, "DAP": 0.2})
