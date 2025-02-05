def palindrom(text):
    check_text = ''.join(simbol.lower() for simbol in text if simbol.isalnum())
    return check_text == check_text[::-1]

user_input = input("Текст или число: ")

if palindrom(user_input):
    print("Палиндром")
else:
    print("Не палиндром")
