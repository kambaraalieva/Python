def to_bin_str(n: int, width: int = 0) -> str:
    s = bin(n)[2:]  # убираем 0b
    if width > 0:
        s = s.zfill(width)  # добавляем ведущие нули
    return s

# Примеры
nums = [5, 2, 10]
for n in nums:
    print(f"{n} -> {to_bin_str(n, 8)}")
