# Northwind Analytics -- Pricing Engine (INTERNAL / PROPRIETARY)
# Confidential -- do not distribute outside Northwind Analytics.
# (Synthetic demo file -- Northwind Analytics is a fictitious company.)

def compute_discount(customer_tier: str, contract_value: float) -> float:
    """Placeholder business logic for demo purposes only."""
    tier_multipliers = {"enterprise": 0.22, "mid_market": 0.14, "smb": 0.06}
    base = tier_multipliers.get(customer_tier, 0.0)
    if contract_value > 250_000:
        base += 0.05
    return round(base, 4)
