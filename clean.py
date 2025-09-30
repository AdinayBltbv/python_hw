import re

def clean_text(text: str) -> str:
    """
    Функция очищает текст от спецсимволов и цифр.
    Оставляет только буквы и пробелы.
    """
    cleaned = re.sub(r'[^a-zA-Zа-яА-ЯёЁ\s]', '', text)
    cleaned = re.sub(r'\s+', ' ', cleaned).strip()
    return cleaned

if __name__ == "__main__":
    user_text = input("Введите текст для очистки: ")
    cleaned_text = clean_text(user_text)

    print("\nИсходный текст:\n", user_text)
    print("\nОчищенный текст:\n", cleaned_text)
