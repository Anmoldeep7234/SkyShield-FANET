import pandas as pd

dataset = pd.read_csv(
    "data/fanet_dataset.csv"
)

print("\n===== DATASET REPORT =====\n")

print(
    dataset["Attack_Type"]
    .value_counts()
)

print(
    "\nTotal Records:",
    len(dataset)
)