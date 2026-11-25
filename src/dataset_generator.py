
import pandas as pd


def create_dataset():

    telemetry = pd.read_csv(
        "data/telemetry.csv"
    )

    dataset = telemetry.copy()

    # Binary label
    dataset["Attack"] = 0

    # Attack type
    dataset["Attack_Type"] = "Normal"

    # Grayhole Detection
    dataset.loc[
        dataset["status"] == "Dropped",
        "Attack"
    ] = 1

    dataset.loc[
        dataset["status"] == "Dropped",
        "Attack_Type"
    ] = "Grayhole"

    # Route Poisoning Detection
    dataset.loc[
        dataset["route_status"] == "Poisoned",
        "Attack"
    ] = 1

    dataset.loc[
        dataset["route_status"] == "Poisoned",
        "Attack_Type"
    ] = "RoutePoisoning"

    dataset.to_csv(
        "data/fanet_dataset.csv",
        index=False
    )

    print(
        "Dataset Generated Successfully!"
    )

    print(
        "Total Records:",
        len(dataset)
    )


if __name__ == "__main__":
    create_dataset()
