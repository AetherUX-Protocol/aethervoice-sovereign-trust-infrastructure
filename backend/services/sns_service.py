# backend/services/sns_service.py

"""
SNS Identity Service
--------------------

Simulated SNS-based trust identity layer
for AetherVoice.

This module demonstrates:
- SNS identity registration
- trust profile creation
- reputation persistence
- trust score history
- transaction reputation tracking

Built for:
SNS Identity Track — Solana Frontier Hackathon
"""

from dataclasses import dataclass, field
from typing import List, Dict


# -----------------------------------
# Identity Model
# -----------------------------------

@dataclass
class TrustProfile:
    sns_identity: str
    total_verified_transactions: int = 0
    successful_settlements: int = 0
    current_trust_score: int = 50
    trust_history: List[int] = field(default_factory=list)


# -----------------------------------
# SNS Identity Service
# -----------------------------------

class SNSIdentityService:

    def __init__(self):
        self.identity_store: Dict[str, TrustProfile] = {}

    # -----------------------------------
    # Register Identity
    # -----------------------------------

    def register_identity(self, sns_name: str) -> TrustProfile:

        if sns_name in self.identity_store:
            return self.identity_store[sns_name]

        profile = TrustProfile(
            sns_identity=sns_name,
            trust_history=[50]
        )

        self.identity_store[sns_name] = profile

        return profile

    # -----------------------------------
    # Update Trust Profile
    # -----------------------------------

    def update_reputation(
        self,
        sns_name: str,
        trust_score: int,
        settlement_successful: bool
    ) -> TrustProfile:

        profile = self.identity_store.get(sns_name)

        if not profile:
            raise ValueError(
                f"SNS identity '{sns_name}' not found."
            )

        profile.total_verified_transactions += 1

        if settlement_successful:
            profile.successful_settlements += 1

        profile.current_trust_score = trust_score
        profile.trust_history.append(trust_score)

        return profile

    # -----------------------------------
    # Fetch Identity Summary
    # -----------------------------------

    def get_identity_summary(
        self,
        sns_name: str
    ) -> Dict:

        profile = self.identity_store.get(sns_name)

        if not profile:
            raise ValueError(
                f"SNS identity '{sns_name}' not found."
            )

        average_score = (
            sum(profile.trust_history)
            / len(profile.trust_history)
        )

        return {
            "sns_identity": profile.sns_identity,
            "verified_transactions":
                profile.total_verified_transactions,
            "successful_settlements":
                profile.successful_settlements,
            "current_trust_score":
                profile.current_trust_score,
            "average_trust_score":
                round(average_score, 2)
        }


# -----------------------------------
# Example Demo Run
# -----------------------------------

if __name__ == "__main__":

    sns_service = SNSIdentityService()

    # Register identity
    profile = sns_service.register_identity(
        "fuelbroker.sol"
    )

    print("\n--- SNS Identity Registered ---\n")

    print(f"SNS Identity: {profile.sns_identity}")
    print(f"Initial Trust Score: {profile.current_trust_score}")

    # Simulate successful settlement
    updated_profile = sns_service.update_reputation(
        sns_name="fuelbroker.sol",
        trust_score=82,
        settlement_successful=True
    )

    # Fetch summary
    summary = sns_service.get_identity_summary(
        "fuelbroker.sol"
    )

    print("\n--- Updated Trust Profile ---\n")

    for key, value in summary.items():
        print(f"{key}: {value}")
