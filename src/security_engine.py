from anomaly_detection import detect_attack
from isolation import (
    isolate_node,
    save_quarantine
)

anomalies = detect_attack()

for _, row in anomalies.iterrows():

    isolate_node(
        row["source"]
    )

save_quarantine()

print(
    "\nQuarantine File Generated"
)

