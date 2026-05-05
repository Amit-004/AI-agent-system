import json
from pathlib import Path

class Verdict:
    def __init__(self, blocked, message):
        self.blocked = blocked
        self.message = message


def check(query):
    q = query.lower()

    # --- insider trading ---
    if any(w in q for w in ["unannounced", "confidential", "earnings before", "tip"]):
        return Verdict(True, "Blocked: insider trading")

    # --- manipulation ---
    if any(w in q for w in ["pump up", "coordinated buying", "wash trade"]):
        return Verdict(True, "Blocked: market manipulation")

    # --- laundering ---
    if any(w in q for w in [
    "avoid reporting",
    "structure deposits",
    "move 500k",
    "obscure the source",
    "hide trading profits"
]):
        return Verdict(True, "Blocked: money laundering")

    # --- guaranteed returns ---
    if any(w in q for w in ["guarantee me", "100% certain", "foolproof", "double in a year"]):
        return Verdict(True, "Blocked: guaranteed returns")

    # --- reckless ---
    if any(w in q for w in ["all my retirement", "entire emergency", "mortgage my house", "margin loan"]):
        return Verdict(True, "Blocked: reckless advice")

    # --- sanctions ---
    if any(w in q for w in ["bypass ofac", "sanctioned russian"]):
        return Verdict(True, "Blocked: sanctions evasion")

    # --- fraud ---
    if "fake contract" in q:
        return Verdict(True, "Blocked: fraud")

    return Verdict(False, "Safe educational query")


    # return Verdict(blocked=False, message="Safe")
