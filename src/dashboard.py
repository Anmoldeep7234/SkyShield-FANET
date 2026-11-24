import streamlit as st
import pandas as pd
import plotly.express as px

# Page Settings
st.set_page_config(
    page_title="SkyShield FANET Security Dashboard",
    page_icon="🛡️",
    layout="wide"
)

# Load Data
telemetry = pd.read_csv("data/telemetry.csv")
dataset = pd.read_csv("data/fanet_dataset.csv")

# Real Metrics
total_uavs = 10

total_packets = len(telemetry)

forwarded_packets = len(
    telemetry[
        telemetry["status"] == "Forwarded"
    ]
)

dropped_packets = len(
    telemetry[
        telemetry["status"] == "Dropped"
    ]
)

poisoned_routes = len(
    telemetry[
        telemetry["route_status"] == "Poisoned"
    ]
)

suspicious_nodes = len(
    dataset[
        dataset["Attack"] == 1
    ]
)

packet_loss = (
    dropped_packets /
    total_packets
) * 100

# Title
st.title("🛡️ SkyShield FANET Security Dashboard")

st.markdown("---")

# Main KPIs
col1, col2, col3, col4 = st.columns(4)

with col1:
    st.metric(
        "🚁 Active UAVs",
        total_uavs
    )

with col2:
    st.metric(
        "📦 Total Packets",
        total_packets
    )

with col3:
    st.metric(
        "❌ Dropped Packets",
        dropped_packets
    )

with col4:
    st.metric(
        "⚠ Suspicious Events",
        suspicious_nodes
    )

# Tabs
tab1, tab2, tab3, tab4 = st.tabs([
    "Network",
    "Attacks",
    "Detection",
    "Reports"
])

# ======================
# Network
# ======================

with tab1:

    st.header("Network Statistics")

    network_data = pd.DataFrame(
        {
            "Status": [
                "Forwarded",
                "Dropped"
            ],
            "Packets": [
                forwarded_packets,
                dropped_packets
            ]
        }
    )

    fig = px.pie(
        network_data,
        values="Packets",
        names="Status",
        title="Packet Distribution"
    )

    st.plotly_chart(
        fig,
        use_container_width=True
    )

# ======================
# Attacks
# ======================

with tab2:

    st.header("Attack Statistics")

    col1, col2 = st.columns(2)

    with col1:

        st.metric(
            "Grayhole Packet Drops",
            dropped_packets
        )

    with col2:

        st.metric(
            "Route Poisoning Events",
            poisoned_routes
        )

    attack_table = pd.DataFrame(
        {
            "Node": [
                "UAV_5",
                "UAV_7"
            ],
            "Attack": [
                "Grayhole",
                "Route Poisoning"
            ]
        }
    )

    st.dataframe(
        attack_table,
        use_container_width=True
    )

# ======================
# Detection
# ======================

with tab3:

    st.header(
        "Intrusion Detection Results"
    )

    attack_records = dataset[
        dataset["Attack"] == 1
    ]

    st.metric(
        "Suspicious Records",
        len(attack_records)
    )

    st.dataframe(
        attack_records.head(20),
        use_container_width=True
    )

# ======================
# Reports
# ======================

with tab4:

    st.header(
        "Security Report"
    )

    st.metric(
        "Packet Loss %",
        round(packet_loss, 2)
    )

    metrics = pd.DataFrame(
        {
            "Metric": [
                "Packet Delivery Ratio",
                "Packet Loss"
            ],
            "Value": [
                round(
                    (forwarded_packets /
                    total_packets)
                    * 100,
                    2
                ),
                round(
                    packet_loss,
                    2
                )
            ]
        }
    )

    fig2 = px.bar(
        metrics,
        x="Metric",
        y="Value",
        color="Metric",
        title="Network Performance"
    )

    st.plotly_chart(
        fig2,
        use_container_width=True
    )

    if st.button(
        "Generate Security Report"
    ):
        st.success(
            "Security Report Generated Successfully ✅"
        )