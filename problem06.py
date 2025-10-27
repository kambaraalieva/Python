def clip(x, low, high):
    if x < low: return low
    if x > high: return high
    return x

# Примеры
tests = [5, -2, 10, 15, 0]
for t in tests:
    print(f"clip({t}, 0, 10) = {clip(t, 0, 10)}")
