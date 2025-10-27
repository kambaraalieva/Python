def filter_nums(nums):
    result = []
    for n in nums:
        if (n % 3 == 0 or n % 5 == 0) and not (n % 3 == 0 and n % 5 == 0):
            result.append(n)
    return result

# Пример
nums = list(range(1, 21))
print(filter_nums(nums))
