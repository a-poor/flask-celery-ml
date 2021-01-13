
import json
import pickle
import numpy as np
from celery import Celery

MODEL_PATH = "model.pkl"

papp = Celery(
    "predict",
    broker="redis://redis"
)


def load_model(path: str):
    with open(path,"rb") as f:
        return pickle.load(f)

def transform_data(input_data: dict):
    # Mean value for each column
    defaults = { 
        'sepal-length': 5.84,
        'sepal-width': 3.06,
        'petal-length': 3.76,
        'petal-width': 1.20
    }
    data = {**defaults,**input_data}
    return np.array([[
        data[k] for k in defaults.keys()
    ]])

def get_predictions(model,data):
    TARGETS = ['setosa','versicolor','virginica']
    preds = model.predict_proba(data)
    return dict(zip(TARGETS,preds[0]))

@papp.task
def predict(input_data: dict):
    model = load_model(MODEL_PATH)
    data = transform_data(input_data)
    preds = get_predictions(model,data)
    return preds

