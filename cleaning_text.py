def clean_text(text: str) -> str:
    cleaned = "".join(ch for ch in text if ch.isalpha() or ch.isspace())
    cleaned = " ".join(cleaned.split())
    return cleaned

if __name__ == "__main__":
    user_text = input("Введите текст для очистки: ")
    cleaned_text = clean_text(user_text)

    print("Исходный текст: ", user_text)
    print(" ")
    print("Очищенный текст: ", cleaned_text)
