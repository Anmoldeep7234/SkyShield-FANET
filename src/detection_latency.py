import time
from anomaly_detection import detect_attack

start = time.time()

detect_attack()

end = time.time()

latency = end - start

print(
    "Detection Latency:",
    round(latency,3),
    "seconds"
)