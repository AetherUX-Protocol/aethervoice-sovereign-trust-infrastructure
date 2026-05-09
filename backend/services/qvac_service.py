# backend/services/qvac_service.py

"""
QVAC Verification Service
-------------------------

Simulated local AI verification pipeline for AetherVoice.

This module demonstrates:
- OCR-style extraction
- semantic verification
- anomaly detection
- urgency signal analysis
- local transaction intelligence

All analysis is designed to represent
local-first AI verification using QVAC.
"""

from typing import Dict, List


# -----------------------------------
# Suspicious Language Patterns
# -----------------------------------

URGENCY_KEYWORDS = [
    "urgent",
    "immediately",
    "asap",
    "within 1 hour",
    "final warning",
    "do not delay"
]

PAYMENT_CHANGE_KEYWORDS = [
    "new account",
    "updated bank details",
    "change payment",
    "send to new wallet",
    "alternate account"
]


# -----------------------------------
# QVAC Verification Engine
# -----------------------------------

class QVACVerificationService:

    def __init__(self):
        pass

    def analyze_document(self, document_text: str) -> Dict:

        detected_flags: List[str] = []

        urgency_detected = False
        payment_change_detected = False

        text = document_text.lower()

        # -----------------------------------
        # Urgency Detection
        # -----------------------------------

        for keyword in URGENCY_KEYWORDS:
            if keyword in text:
                urgency_detected = True
                detected_flags.append(
                    f"Urgency phrase detected: '{keyword}'"
                )

        # -----------------------------------
        # Payment Change Detection
        # -----------------------------------

        for keyword in PAYMENT_CHANGE_KEYWORDS:
            if keyword in text:
                payment_change_detected = True
                detected_flags.append(
                    f"Payment instruction change detected: '{keyword}'"
                )

        # -----------------------------------
        # Risk Evaluation
        # -----------------------------------

        risk_level = self.calculate_risk(
            urgency_detected,
            payment_change_detected
        )

        # -----------------------------------
        # Final Response
        # -----------------------------------

        return {
            "urgency_detected": urgency_detected,
            "payment_change_detected": payment_change_detected,
            "risk_level": risk_level,
            "flags": detected_flags
        }

    # -----------------------------------
    # Risk Logic
    # -----------------------------------

    def calculate_risk(
        self,
        urgency: bool,
        payment_change: bool
    ) -> str:

        if urgency and payment_change:
            return "High"

        elif urgency or payment_change:
            return "Medium"

        return "Low"


# -----------------------------------
# Example Demo Run
# -----------------------------------

if __name__ == "__main__":

    sample_document = """
    Dear Partner,

    Please process this payment immediately.

    Due to banking changes, send funds to the
    updated bank details attached in this email.

    Do not delay settlement.

    Regards,
    Operations Team
    """

    qvac = QVACVerificationService()

    result = qvac.analyze_document(sample_document)

    print("\n--- QVAC Verification Result ---\n")

    print(f"Risk Level: {result['risk_level']}")
    print(f"Urgency Detected: {result['urgency_detected']}")
    print(
        f"Payment Change Detected: "
        f"{result['payment_change_detected']}"
    )

    print("\nFlags:")

    if result["flags"]:
        for flag in result["flags"]:
            print(f"- {flag}")

    else:
        print("- No suspicious signals detected.")
