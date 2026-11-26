import pandas as pd

quarantine = []

def isolate_node(node):

    if node not in quarantine:
        quarantine.append(node)

    return quarantine

def save_quarantine():

    df = pd.DataFrame(
        {
            "Node": quarantine
        }
    )

    df.to_csv(
        "data/quarantine_nodes.csv",
        index=False
    )