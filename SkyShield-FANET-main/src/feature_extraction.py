import pandas as pd

def calculate_metrics():
    # Đọc dữ liệu telemetry
    df = pd.read_csv("data/telemetry.csv")

    total = len(df)

    forwarded = len(df[df["status"] == "Forwarded"])

    dropped = len(df[df["status"] == "Dropped"])

    pdr = forwarded / total if total > 0 else 0

    loss = dropped / total if total > 0 else 0

    metrics = {
        "Total_Packets": total,
        "Forwarded": forwarded,
        "Dropped": dropped,
        "PDR": round(pdr, 2),
        "Packet_Loss": round(loss, 2)
    }

    return metrics

if __name__ == "__main__":
    print("Calculated Metrics Output:")
    print(calculate_metrics())