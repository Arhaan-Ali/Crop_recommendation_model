# Project Guidelines

## Code Style
- **Python**: Follows PEP8 with some practical flexibility. Indentation is 4 spaces. Type hints are not enforced. See `crop_type_recommendation.py` and `fertilizer_logic.py` for typical style.
- **TensorFlow/Keras and PyTorch**: Use standard API idioms. See `fertilizer_recommendation_neural.py` and `soil_type_classifier.py` for model code patterns.
- **DataFrames**: Use pandas idioms for data manipulation, e.g., `df.drop`, `df.duplicated()`, `df.info()`.

## Architecture
- **Main scripts**: Each major ML task has a dedicated script:
  - `crop_type_recommendation.py`: Crop recommendation (RandomForest)
  - `fertilizer_logic.py`: Fertilizer logic (rule-based + ML)
  - `fertilizer_recommendation_neural.py`: Fertilizer recommendation (Neural Net)
  - `soil_type_classifier.py`: Soil image classification (PyTorch)
- **Data**: Expects CSVs in `Dataset/` and images in `Dataset/Train`, `Dataset/Test`, `Dataset/Validate`.
- **Models**: Models are saved as `.pkl` (pickle) or `.pt` (PyTorch) in the project root.

## Build and Test
- **Install dependencies**: `pip install -r requirements.txt` (ensure to update this file as needed)
- **Run scripts**: Execute each script directly, e.g., `python crop_type_recommendation.py`
- **Docker**: Use the `Dockerfile` for containerized runs (currently minimal, extend as needed).
- **Testing**: No formal test suite; validate by running scripts and checking printed metrics/outputs.

## Project Conventions
- **No formal package structure**: Scripts are flat in the root, with one subfolder `src/` (currently empty).
- **Model saving**: Use `pickle.dump` for sklearn/keras models, `torch.save` for PyTorch.
- **Data paths**: Hardcoded relative paths to `Dataset/`.
- **No CLI/REST API yet**: All scripts are run as main modules.

## Integration Points
- **External dependencies**:
  - `scikit-learn`, `pandas`, `matplotlib`, `seaborn`, `torch`, `torchvision`, `tensorflow`, `keras`
- **No external APIs**: All logic is local.

## Security
- **No authentication or secrets**: All data and models are local. No sensitive information handled.
- **Pickle warning**: Only load pickle files you trust (see `fertilizer_logic.py`, `fertilizer_recommendation_neural.py`).

---

If you add new scripts, models, or data sources, update this file with new conventions or patterns. For questions, review the main scripts for examples of style and structure.