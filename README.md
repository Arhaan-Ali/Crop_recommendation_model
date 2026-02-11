# Crop Recommendation Model API

This project provides a FastAPI-based web API for crop, fertilizer, and soil type recommendations using machine learning models.

## Features
- Crop recommendation based on soil and weather parameters
- Fertilizer recommendation (rule-based and neural network)
- Soil type classification from images

## Project Structure
```
app/
  main.py            # FastAPI entrypoint
  routers/           # API endpoints
  models/            # Pydantic schemas
  services/          # Business/model logic
Dataset/              # Data files (ignored by git)
```

## Setup
1. **Clone the repository**
2. **Install dependencies**
   ```sh
   pip install -r requirements.txt
   ```
3. **(Optional) Build Docker image**
   ```sh
   docker build -t crop-recommendation-fastapi .
   ```

## Running the API
### Locally
```sh
python -m uvicorn app.main:app --reload
```

### With Docker
```sh
docker run -p 8000:8000 crop-recommendation-fastapi
```

## API Endpoints
- `POST /crop/recommend` — Crop recommendation
- `POST /fertilizer/logic` — Fertilizer logic recommendation
- `POST /fertilizer/neural` — Fertilizer neural net recommendation
- `POST /soil/type` — Soil type classification

See interactive docs at: [http://127.0.0.1:8000/docs](http://127.0.0.1:8000/docs)


## Example Requests

### Crop Recommendation
**POST** `/crop/recommend`
```json
{
  "N": 90,
  "P": 40,
  "K": 40,
  "temperature": 25.0,
  "humidity": 80.0,
  "ph": 6.5,
  "rainfall": 200.0
}
```

### Fertilizer Logic Recommendation
**POST** `/fertilizer/logic`
```json
{
  "state": "Delhi",
  "sample": [90, 40, 40, 1.2, 0.5, 0.3, 0.2, 0.1, 0.1, 0.1]
}
```

### Fertilizer Neural Recommendation
**POST** `/fertilizer/neural`
```json
{
  "features": [90, 40, 40, 1.2, 0.5, 0.3, 0.2, 0.1, 0.1, 0.1]
}
```

### Soil Type Classification
**POST** `/soil/type`
```json
{
  "image_path": "Dataset/Test/soil1.jpg"
}
```

## Notes
- Model files (`.pkl`, `.pt`) and data are not included in the repo.
- All endpoints currently return dummy responses for testing.
- Update the service logic to load and use your trained models.

---

For questions or contributions, open an issue or pull request.
