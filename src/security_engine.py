from anomaly_detection import detect_attack
from isolation import isolate_node

anomalies = detect_attack()

for _, row in anomalies.iterrows():

    isolate_node(
        row["source"]
    )

print("\nQuarantine List:")