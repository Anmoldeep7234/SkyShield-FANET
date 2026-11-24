quarantine = []

def isolate_node(node):

    if node not in quarantine:

        quarantine.append(node)

        print(
            f"{node} moved to quarantine"
        )

    return quarantine