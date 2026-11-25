import pandas as pd

from sklearn.ensemble import IsolationForest

def detect_attack():

    df = pd.read_csv(
        "data/fanet_dataset.csv"
    )