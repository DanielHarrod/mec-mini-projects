import pickle
import os
import numpy as np
from pathlib import Path

filename = 'extra_trees_classifier.pickle'
from sklearn.ensemble import ExtraTreesClassifier

import warnings
warnings.filterwarnings("ignore")

class Model:
    def __init__(self, model_path: str = None):
        self._model = None
        self._model_path = model_path
        self.load()

    def predict(self, X: np.ndarray) -> np.ndarray:
    
        return self._model.predict(X)

    def load(self):
        self._model = pickle.load(open(model_path, "rb"))
        return self

model_path = Path(__file__).parent / filename
if ( os.path.isfile(model_path) ):
    model = Model(model_path)
else:
    model = Model()

n_features = 20

def get_model():
    return model

if __name__ == '__main__':
    model = Model()
    print(model.predict(np.array([[1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1]])))