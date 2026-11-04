from src.simulator import generate_packet
from src.attack import apply_attack
from src.packet_capture import save_packet

TOTAL_PACKETS = 1000

forwarded = 0
dropped = 0

print("Simulation Started...")

for i in range(TOTAL_PACKETS):

    packet = generate_packet()

    packet = apply_attack(packet)

    save_packet(packet)

    if packet["status"] == "Forwarded":
        forwarded += 1
    else:
        dropped += 1

print("\n=== RESULTS ===")
print("Packets Generated:", TOTAL_PACKETS)
print("Forwarded:", forwarded)
print("Dropped:", dropped)