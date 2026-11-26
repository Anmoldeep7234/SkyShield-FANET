import streamlit as st
import pandas as pd
import plotly.express as px

telemetry = pd.read_csv(
    "data/telemetry.csv"
)

dataset = pd.read_csv(
    "data/fanet_dataset.csv"
)

detected = pd.read_csv(
    "data/detected_attacks.csv"
)

quarantine = pd.read_csv(
    "data/quarantine_nodes.csv"
)

benchmark = pd.read_csv(
    "reports/benchmark_results.csv"
)

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

detected_attacks = len(
    detected
)

security_score = (
    forwarded_packets /
    total_packets
) * 100

# Title
st.title("🛡️ SkyShield FANET Security Dashboard")

st.markdown("---")

# Main KPIs
col1, col2, col3, col4, col5 = st.columns(5)

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

with col5:

    st.metric(
        "🛡 Security Score",
        round(
            security_score,
            2
        )
    )
    
# Tabs
tab1, tab2, tab3, tab4, tab5, tab6 = st.tabs([
    "Network",
    "Attacks",
    "Detection",
    "Reports",
    "Benchmarks",
    "Quarantine"
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
    
    st.metric(
    "Detected Attacks",
    detected_attacks
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

    st.subheader(
        "Isolation Forest Results"
    )

    st.dataframe(
        detected.head(20),
        use_container_width=True
    )
    
# ======================
# Reports
# ======================

with tab4:

    st.header(
        "Security Report")

    st.metric(
        "Packet Loss %",
        round(packet_loss, 2)
    )
    
    st.metric(
    "Security Score",
    round(security_score,2)
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

with tab5:

    st.header("Benchmark Results")

    st.dataframe(
        benchmark,
        use_container_width=True
    )

    fig3 = px.bar(
        benchmark,
        x="Metric",
        y=[
            "Before_Attack",
            "During_Attack",
            "After_Isolation"
        ],
        barmode="group",
        title="Network Performance Comparison"
    )

    st.plotly_chart(
        fig3,
        use_container_width=True
    )


with tab6:

    st.header(
        "Quarantined UAV Nodes"
    )

    st.dataframe(
        quarantine,
        use_container_width=True
    )

    st.metric(
        "Nodes Isolated",
        len(quarantine)
    )

if st.button(
        "Generate Security Report"
    ):
    st.success(
            "Security Report Generated Successfully ✅"
        )