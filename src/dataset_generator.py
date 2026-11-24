import pandas as pd

def create_dataset():

    telemetry = pd.read_csv(
        "data/telemetry.csv"
    )

    dataset = telemetry.copy()

    dataset["Attack"] = 0

    dataset.loc[
        dataset["status"] == "Dropped",
        "Attack"
    ] = 1

    dataset.loc[
        dataset["route_status"] == "Poisoned",
        "Attack"
    ] = 1

    dataset.to_csv(
        "data/fanet_dataset.csv",
        index=False
    )

    print(
        "Dataset Saved Successfully"
    )

if __name__ == "__main__":
    create_dataset()