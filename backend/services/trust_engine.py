# backend/trust_engine.py

"""
AetherVoice Trust Engine
------------------------

Core trust evaluation logic for high-risk commerce verification.

This module simulates:
- transaction verification
- anomaly detection
- trust scoring
- risk evaluation
- settlement recommendation

Built for:
SNS Identity Track — Solana Frontier Hackathon
"""

from dataclasses import dataclass
from typing import List, Dict
import random


# -----------------------------
# Transaction Model
# -----------------------------

@dataclass
class TransactionContext:
    broker_name: str
    invoice_amount: float
    payment_country: str
    urgency_detected: bool
    payment_instruction_changed: bool
    inconsistent_language: bool
    prior_verified_transactions: int


# -----------------------------
# Trust Engine
# -----------------------------

class AetherVoiceTrustEngine:

    def __init__(self):
        self.base_score = 50

    def evaluate_transaction(self, tx: TransactionContext) -> Dict:

        score = self.base_score
        risk_flags: List[str] = []

        # -----------------------------------
        # Positive Signals
        # -----------------------------------

        if tx.prior_verified_transactions > 5:
            score += 20

        elif tx.prior_verified_transactions > 0:
            score += 10

        # -----------------------------------
        # Risk Signals
        # -----------------------------------

        if tx.urgency_detected:
            score -= 15
            risk_flags.append(
                "Urgency manipulation detected in communication."
            )

        if tx.payment_instruction_changed:
            score -= 25
            risk_flags.append(
                "Payment instructions changed during transaction flow."
            )

        if tx.inconsistent_language:
            score -= 10
            risk_flags.append(
                "Inconsistent communication patterns identified."
            )

        # -----------------------------------
        # Score Boundaries
        # -----------------------------------

        score = max(0, min(score, 100))

        # -----------------------------------
        # Recommendation Logic
        # -----------------------------------

        if score >= 75:
            recommendation = "Proceed"

        elif score >= 45:
            recommendation = "Caution"

        else:
            recommendation = "Stop"

        # -----------------------------------
        # Final Response
        # -----------------------------------

        return {
            "broker": tx.broker_name,
            "trust_score": score,
            "recommendation": recommendation,
            "risk_flags": risk_flags
        }


# -----------------------------
# Example Demo Run
# -----------------------------

if __name__ == "__main__":

    sample_transaction = TransactionContext(
        broker_name="Global Fuel Broker LLC",
        invoice_amount=250000,
        payment_country="UAE",
        urgency_detected=True,
        payment_instruction_changed=True,
        inconsistent_language=False,
        prior_verified_transactions=2
    )

    engine = AetherVoiceTrustEngine()

    result = engine.evaluate_transaction(sample_transaction)

    print("\n--- AetherVoice Trust Evaluation ---\n")

    print(f"Broker: {result['broker']}")
    print(f"Trust Score: {result['trust_score']}")
    print(f"Recommendation: {result['recommendation']}")

    print("\nRisk Flags:")

    if result["risk_flags"]:
        for flag in result["risk_flags"]:
            print(f"- {flag}")

    else:
        print("- No major risks detected.")
