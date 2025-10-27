def read_number(prompt):
    while True:
        val = input(prompt)
        try:
            if '.' in val:
                return float(val)
            else:
                return int(val)
        except ValueError:
            print("Ошибка: введите корректное число")

