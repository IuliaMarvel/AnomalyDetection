import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

from sklearn.model_selection import train_test_split
from sklearn.linear_model import LogisticRegression
from sklearn.metrics import accuracy_score, classification_report

from data_preprocess import json_to_dataframe, preprocess_dataframe
import argparse
import pickle
import os



def train_and_save_model(data_path='synthetic_tls_data.json', target_column='is_anomaly', test_size=0.2, random_seed=42, C=1.0, models_path='models'):

    os.makedirs(models_path, exist_ok=True)

    df = json_to_dataframe(data_path)
    df = preprocess_dataframe(df)
    X = df.drop(columns=[target_column])
    y = df[target_column]
    
    X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=test_size, random_state=random_seed)
    print(f'Samples in train: {len(y_train)}')
    print(f'Samples in test: {len(y_test)}')
    model = LogisticRegression(C=C, random_state=random_seed)
    model.fit(X_train, y_train)
    y_pred = model.predict(X_test)
    
    accuracy = accuracy_score(y_test, y_pred)
    class_report = classification_report(y_test, y_pred)

    print(f'Accuracy: {round(accuracy, 3)}')
    print(class_report)

    
    model_filename = f"models/model_{random_seed}_{C}.pkl"
    with open(model_filename, 'wb') as f:
        pickle.dump(model, f)
    
    print(f'Model saved at {model_filename}')

    return accuracy


if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="Train anomaly detection model.")
    parser.add_argument("--test_size", type=float, default=0.2, help="Fraction of data used for test.")
    parser.add_argument("--C", type=float, default=0.5, help="Regularization for LogRegression.")
    parser.add_argument("--seed", type=int, default=0, help="Random seed for train/test split reproducibility.")
    args = parser.parse_args()

    _ = train_and_save_model(test_size=args.test_size, random_seed=args.seed, C=args.C)
