from flask import Flask, request, jsonify

import pandas as pd
from data_preprocess import json_to_dataframe, preprocess_dataframe
from train_pipeline import train_and_save_model

import os
import pickle

app = Flask(__name__)

MODEL_DIR = "models"
if not os.path.exists(MODEL_DIR):
    os.makedirs(MODEL_DIR)


def load_model(model_filename: str):
    with open(model_filename, 'rb') as f:
        model = pickle.load(f)
    return model


@app.route("/predict", methods=["POST"])
def predict():

    model = load_model(os.path.join(MODEL_DIR, os.listdir(MODEL_DIR)[-1])) # load last model (for example)
    df = pd.DataFrame(request.get_json(), index=[0])
    df = preprocess_dataframe(df)
        
    prediction = model.predict(df)
    
    return jsonify({"is_anomaly": round(prediction[0])})

@app.route("/train", methods=["POST"])
def train():
    seed = request.json.get("seed", 42)
    C = request.json.get("C", 1.0)
    accuracy = train_and_save_model(random_seed=seed, C=C)
    
    return jsonify({
        "message": "Model trained successfully",
        "accuracy": accuracy
    })


if __name__ == "__main__":
    app.run(host="0.0.0.0", port=8000)
