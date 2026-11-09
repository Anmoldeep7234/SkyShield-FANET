import pandas as pd
import os

FILE_NAME = "data/telemetry.csv"

def save_packet(packet):

    df = pd.DataFrame([packet])

    if not os.path.exists(FILE_NAME):
        df.to_csv(FILE_NAME, index=False)

    else:
        df.to_csv(
            FILE_NAME,
            mode="a",
            header=False,
            index=False
        )