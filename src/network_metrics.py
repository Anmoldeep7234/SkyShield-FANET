import pandas as pd

def calculate_benchmarks():

    telemetry = pd.read_csv(
        "data/telemetry.csv"
    )

    total_packets = len(
        telemetry
    )

    forwarded = len(
        telemetry[
            telemetry["status"] ==
            "Forwarded"
        ]
    )

    dropped = len(
        telemetry[
            telemetry["status"] ==
            "Dropped"
        ]
    )

    pdr = (
        forwarded /
        total_packets
    ) * 100

    loss = (
        dropped /
        total_packets
    ) * 100

    avg_delay = telemetry[
        "delay"
    ].mean()

    avg_hops = telemetry[
        "hop_count"
    ].mean()

    print("\nBENCHMARK RESULTS")

    print(
        "Packet Delivery Ratio:",
        round(pdr,2)
    )

    print(
        "Packet Loss:",
        round(loss,2)
    )

    print(
        "Average Delay:",
        round(avg_delay,2)
    )

    print(
        "Average Hop Count:",
        round(avg_hops,2)
    )

if __name__ == "__main__":
    calculate_benchmarks()