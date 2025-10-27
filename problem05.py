def eval_simple(expr: str):
    try:
        a_str, op, b_str = expr.split()
        a = float(a_str) if '.' in a_str else int(a_str)
        b = float(b_str) if '.' in b_str else int(b_str)
        if op == '+': return a + b
        if op == '-': return a - b
        if op == '*': return a * b
        if op == '/': return a / b
        if op == '//': return a // b
        if op == '%': return a % b
        if op == '**': return a ** b
        raise ValueError("Неверная операция")
    except ZeroDivisionError:
        return "Ошибка: деление на ноль"
    except Exception as e:
        return f"Ошибка: {e}"

# Примеры
expressions = ["10 + 5", "10 / 0", "3 ** 2", "7 // 3", "10 % 3", "4.5 * 2"]
for ex in expressions:
    print(f"{ex} = {eval_simple(ex)}")
