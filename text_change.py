def text_change(text, new_letter):
    text = ''.join(char for i, char in enumerate(text) if i % 2 == 0)
    text = text.replace("и", new_letter).replace("Я", new_letter.upper())

    return text

text_by_user = input("Введите текст: ")
if "и" in text_by_user or "И" in text_by_user:
    new_text = input("Введите букву, на которую заменить 'и': ")
else:
    new_text=''

text_changed = text_change(text_by_user, new_text)
print("Измененный текст: ", text_changed)