# ai/qvac/semantic_analysis.py

"""
QVAC Semantic Analysis
----------------------

Simulated semantic verification
for transaction communications.
"""

from typing import Dict


SUSPICIOUS_PATTERNS = [
    "urgent",
    "change payment",
    "new account",
    "confidential request"
]


def analyze_semantics(
    text: str
) -> Dict:

    detected_patterns = []

    lower_text = text.lower()

    for pattern in SUSPICIOUS_PATTERNS:

        if pattern in lower_text:
            detected_patterns.append(pattern)

    return {
        "patterns_detected": detected_patterns,
        "risk_score": len(detected_patterns) * 20
    }


# Example Demo Run

if __name__ == "__main__":

    sample_text = (
        "Urgent settlement required. "
        "Please use new account details."
    )

    result = analyze_semantics(sample_text)

    print(result)
