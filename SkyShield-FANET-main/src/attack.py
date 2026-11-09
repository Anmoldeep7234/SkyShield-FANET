import random

MALICIOUS_NODE = "UAV_5"

def apply_attack(packet):

    if packet["source"] == MALICIOUS_NODE:

        if random.random() < 0.55:
            packet["status"] = "Dropped"

        else:
            packet["status"] = "Forwarded"

    else:
        packet["status"] = "Forwarded"

    return packet