import pandas as pd

def calculate_metrics():

    df = pd.read_csv("data/telemetry.csv")

    total_packets = len(df)

    forwarded = len(
        df[df["status"] == "Forwarded"]
    )

    dropped = len(
        df[df["status"] == "Dropped"]
    )

    pdr = forwarded / total_packets

    packet_loss = dropped / total_packets

    avg_delay = df["delay"].mean()

    avg_hops = df["hop_count"].mean()

    avg_packet_size = df["packet_size"].mean()

    metrics = {
        "Total_Packets": total_packets,
        "Forwarded": forwarded,
        "Dropped": dropped,
        "PDR": round(pdr, 3),
        "Packet_Loss": round(packet_loss, 3),
        "Average_Delay": round(avg_delay, 2),
        "Average_Hops": round(avg_hops, 2),
        "Average_Packet_Size": round(avg_packet_size, 2)
    }

    return metrics


if __name__ == "__main__":

    print("\n=== NETWORK METRICS ===")

    print(calculate_metrics())