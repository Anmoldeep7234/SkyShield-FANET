import pandas as pd 
from sklearn.ensemble import IsolationForest

def detect_attack():

    df = pd.read_csv(
        "data/fanet_dataset.csv"
    )

    features = df[
        [
            "hop_count",
            "delay",
            "packet_size"
        ]
    ]

    model = IsolationForest(
        contamination=0.1,
        random_state=42
    )

    predictions = model.fit_predict(
        features
    )

    df["Prediction"] = predictions

    anomalies = df[
        df["Prediction"] == -1
    ]

    anomalies.to_csv(
        "data/detected_attacks.csv",
        index=False
    )

    print(
        "Detected Records:",
        len(anomalies)
    )

    return anomalies

if __name__ == "__main__":
    detect_attack()

    