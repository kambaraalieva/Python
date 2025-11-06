def to_bin_str(n: int, width: int = 0) -> str:
    s = bin(n)[2:]  
    if width > 0:
        s = s.zfill(width)
    return s

# Примеры
nums = [5, 2, 10]
for n in nums:
    print(f"{n} -> {to_bin_str(n, 8)}")
