# ai/qvac/anomaly_detection.py

"""
QVAC Anomaly Detection
----------------------

Simulated anomaly detection engine
for transaction verification.
"""

from typing import Dict


def detect_anomalies(
    payment_changed: bool,
    unusual_urgency: bool
) -> Dict:

    anomalies = []

    if payment_changed:
        anomalies.append(
            "Payment instructions changed."
        )

    if unusual_urgency:
        anomalies.append(
            "Urgency manipulation detected."
        )

    return {
        "anomalies": anomalies,
        "anomaly_count": len(anomalies)
    }


# Example Demo Run

if __name__ == "__main__":

    result = detect_anomalies(
        payment_changed=True,
        unusual_urgency=True
    )

    print(result)
