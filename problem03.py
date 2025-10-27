# 1. Ввод строки
text = input("Введите строку: ")

# 2. Создаём пустой словарь для частот
freq = {} # 

# 3. Считаем символы
for char in text:
    if char in freq:
        freq[char] += 1
    else:
        freq[char] = 1

# 4. Сортируем по убыванию частоты
sorted_items = sorted(freq.items(), key=lambda x: x[1], reverse=True)

# 5. Выводим 5 самых частых символов
print("5 самых частых символов:")
for char, count in sorted_items[:5]:
    print(f"'{char}': {count}")
