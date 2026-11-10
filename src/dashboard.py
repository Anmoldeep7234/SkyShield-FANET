import streamlit as st
import pandas as pd
import plotly.express as px

st.set_page_config(
    page_title="SkyShield FANET Security Dashboard",
    page_icon="🛡️",
    layout="wide"
)

st.title("🛡️ SkyShield FANET Security Dashboard")
st.markdown("---")

# Dummy values for now
total_uavs = 10
total_packets = 1000
dropped_packets = 58
suspicious_nodes = 1

# Top Metrics
col1, col2, col3, col4 = st.columns(4)

with col1:
    st.metric("🚁 Active UAVs", total_uavs)

with col2:
    st.metric("📦 Total Packets", total_packets)

with col3:
    st.metric("❌ Dropped Packets", dropped_packets)

with col4:
    st.metric("⚠️ Suspicious Nodes", suspicious_nodes)

st.markdown("---")

# Network Status
col1, col2 = st.columns(2)

with col1:

    st.subheader("Network Status")

    network_data = pd.DataFrame({
        "Status": ["Forwarded", "Dropped"],
        "Packets": [942, 58]
    })

    fig = px.pie(
        network_data,
        values="Packets",
        names="Status",
        title="Packet Distribution"
    )

    st.plotly_chart(fig, use_container_width=True)

with col2:

    st.subheader("Attack Status")

    attack_data = pd.DataFrame({
        "Node": ["UAV_5"],
        "Attack": ["Grayhole"],
        "Drop Rate": ["55%"]
    })

    st.dataframe(attack_data, use_container_width=True)

st.markdown("---")

# Performance Metrics
st.subheader("📊 Performance Metrics")

metrics = pd.DataFrame({
    "Metric": [
        "Packet Delivery Ratio",
        "Packet Loss Rate",
        "Network Availability",
        "Attack Detection Rate"
    ],
    "Value": [
        94,
        6,
        98,
        92
    ]
})

fig2 = px.bar(
    metrics,
    x="Metric",
    y="Value",
    color="Metric",
    title="Network Performance"
)

st.plotly_chart(fig2, use_container_width=True)

st.markdown("---")

# Node Table

st.subheader("🚁 UAV Network Nodes")

node_table = pd.DataFrame({
    "Node": [
        "UAV_1",
        "UAV_2",
        "UAV_3",
        "UAV_4",
        "UAV_5",
        "UAV_6",
        "UAV_7",
        "UAV_8",
        "UAV_9",
        "UAV_10"
    ],
    "Status": [
        "Active",
        "Active",
        "Active",
        "Active",
        "Suspicious",
        "Active",
        "Active",
        "Active",
        "Active",
        "Active"
    ]
})

st.dataframe(node_table, use_container_width=True)

st.markdown("---")

if st.button("Generate Security Report"):
    st.success("Security Report Generated Successfully ✅")