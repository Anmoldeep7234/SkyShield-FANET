from anomaly_detection import detect_attack
from isolation import (
    isolate_node,
    save_quarantine
)

# Run Isolation Forest detection
anomalies = detect_attack()

# Generate security report
anomalies.to_csv(
    "data/security_report.csv",
    index=False
)

# Isolate suspicious nodes
for _, row in anomalies.iterrows():

    isolate_node(
        row["source"]
    )

# Save quarantine list
save_quarantine()

print(
    "\nQuarantine File Generated"
)

print(
    "Security Report Generated"
)

