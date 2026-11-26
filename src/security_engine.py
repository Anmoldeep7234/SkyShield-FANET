from anomaly_detection import detect_attack
from isolation import (
    isolate_node,
    save_quarantine
)

anomalies = detect_attack()

# Create security report
anomalies.to_csv(
    "data/security_report.csv",
    index=False
)

for _, row in anomalies.iterrows():

    isolate_node(
        row["source"]
    )

save_quarantine()

print("\nSecurity Report Generated")
print("Quarantine File Generated")
