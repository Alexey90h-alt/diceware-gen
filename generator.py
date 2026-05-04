import secrets # Используем безопасный рандом, а не обычный!

def get_diceware_digit():
    # Имитируем бросок кубика (от 1 до 6)
    return str(secrets.randbelow(6) + 1)

def generate_code():
    # Генерируем 5 цифр для одного слова
    return "".join([get_diceware_digit() for _ in range(5)])

# Пример работы
print(f"Ваш код для словаря: {generate_code()}")
