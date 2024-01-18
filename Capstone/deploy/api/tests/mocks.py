import numpy as np

from typing import List

from ..ml.model import Model, get_model, n_features
from pydantic import BaseModel, ValidationError, validator

class PredictResponse(BaseModel):
    data: List[List[float]]
    
class MockModel:
    def __init__(self, model_path: str = None):
        self._model_path = None
        self._model = None

    def predict(self, X: np.ndarray) -> np.ndarray:
        model = get_model()
        y_pred = model.predict(X)
        result = PredictResponse(data=y_pred.tolist())
        return result
    
    def train(self, X: np.ndarray, y: np.ndarray):
        return self

    def save(self):
        pass

    def load(self):
        return self
