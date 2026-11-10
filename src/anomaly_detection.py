from sklearn.ensemble import IsolationForest

def detect_attack(data):

    model = IsolationForest(
        contamination=0.1
    )

    return model