import json
import os
import pickle

import pandas as pd
from sklearn.preprocessing import LabelEncoder


def json_to_dataframe(json_file):
    with open(json_file, "r") as f:
        data = json.load(f)
    return pd.DataFrame(data)


def preprocess_dataframe(df, encoders_path="encoders", verbose=False):
    os.makedirs(encoders_path, exist_ok=True)

    df["browser"] = df["user_agent"].str.extract(r"^(.*?)\(")[0]
    df["os"] = df["user_agent"].str.extract(r"\((.*?)\)")[0]

    tls_components = ["version", "cipher", "extensions", "curves"]
    df[tls_components] = df["tls_ja3"].str.split(",", expand=True)

    encoders = {}
    categorical_features = ["browser", "os"] + tls_components

    for col in categorical_features:
        encoder_file = os.path.join(encoders_path, f"{col}_encoder.pkl")

        if os.path.exists(encoder_file):
            if verbose:
                print(f'Encoder for {col} already exists')
            with open(encoder_file, "rb") as f:
                encoder = pickle.load(f)
            df[col] = encoder.transform(df[col])  
        else:
            encoder = LabelEncoder()
            df[col] = encoder.fit_transform(df[col])
            with open(encoder_file, "wb") as f:
                pickle.dump(encoder, f)
            if verbose:
                print(f'Encoder for {col} was saved.')

    df.drop(['user_agent', 'tls_ja3'], axis=1, inplace=True)

    return df