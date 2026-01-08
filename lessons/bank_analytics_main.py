
def total_balance(accounts: list[dict])
    return sum(acc["balance"] for acc in accounts)

def count_rich(accounts: list[dict], threshold: float) -> int:
    return sum(1 for acc in accounts if acc ["balance"] > threshold)

