
def clean_phone(phone: str):
    return phone.replace("+", "").replace("-", "").replace(" ", "")

def kgs_to_usd(amount_kgs: float, rate: float = 89.0):
    return amount_kgs / rate

