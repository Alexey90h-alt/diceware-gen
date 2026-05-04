import secrets

# Наш тестовый словарик
wordlist = {
    "11111": "apple", "11112": "banana", "11113": "cactus",
    "22222": "ocean", "33333": "mountain", "44444": "forest",
    "55555": "desert", "66666": "zebra"
}

def get_word():
    # Имитируем 5 бросков кубика
    roll = "".join([str(secrets.randbelow(6) + 1) for _ in range(5)])
    # Берем слово из словаря или случайное, если кода нет в мини-списке
    return wordlist.get(roll, secrets.choice(list(wordlist.values())))

def main():
    print("--- Генератор Diceware паролей ---")
    try:
        count = int(input("Сколько слов нужно в пароле? (например, 4): "))
        password = "-".join([get_word() for _ in range(count)])
        print(f"\nВаш безопасный пароль: {password}")
    except ValueError:
        print("Ошибка: введите число!")

if __name__ == "__main__":
    main()
