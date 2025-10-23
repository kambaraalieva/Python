def is_strong(pwd: str) -> bool:
    if len(pwd) < 8:
        return False
    if any(c.isupper() for c in pwd) == False:
        return False
    if any(c.islower() for c in pwd) == False:
        return False
    if any(c.isdigit() for c in pwd) == False:
        return False
    if ' ' in pwd:
        return False
    return True

# Примеры
examples = ["Password1", "pass1", "PASSWORD1", "Pass word1", "Strong123", "Abcdefg8", "ValidPass9"]
for pwd in examples:
    print(f"{pwd}: {is_strong(pwd)}")
