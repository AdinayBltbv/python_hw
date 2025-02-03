def remove_letter():
    text = input("Введите текст: ")
    letters = input("Введите букву, которую нужно удалить: ")

    for letter in letters:
        text = text.replace(letter,"")

    print("Результат: ",text)

remove_letter()