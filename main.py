from src.simulator import generate_packet
from src.attack import apply_attack
from src.packet_capture import save_packet

TOTAL_PACKETS = 1000

forwarded = 0
dropped = 0
poisoned = 0

print("=" * 50)
print("SkyShield FANET Security System")
print("=" * 50)
print("Simulation Started...\n")

for i in range(TOTAL_PACKETS):

    packet = generate_packet()

    packet = apply_attack(packet)

    save_packet(packet)

    # Count forwarded and dropped packets
    if packet["status"] == "Forwarded":
        forwarded += 1
    else:
        dropped += 1

    # Count route poisoning attacks
    if packet["route_status"] == "Poisoned":
        poisoned += 1

print("\n===== RESULTS =====")

print("Packets Generated :", TOTAL_PACKETS)
print("Forwarded Packets :", forwarded)
print("Dropped Packets   :", dropped)
print("Poisoned Routes   :", poisoned)

print("\nSimulation Completed Successfully")