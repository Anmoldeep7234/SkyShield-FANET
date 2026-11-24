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

    print(
        "\nSuspicious Records Found:",
        len(anomalies)
    )

    return anomalies


if __name__ == "__main__":

    anomalies = detect_attack()

    print(anomalies.head())

    