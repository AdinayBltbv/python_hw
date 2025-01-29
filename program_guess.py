import random

def program_guess():
    print("Загадайте число от 1 до 1000, и я попробую его угадать!")

    low = 1
    high =1000
    attempts = 0

    while True:
        guess = (low+high) // 2
        attempts += 1
        print(f"Mоё предположение:{guess}")
        feedback = input("Введи 'меньше', 'больше' или 'верно, угадал!'").strip().lower()

        if feedback == "верно, угадал!":
           print(f"Я угадал число {guess} за {attempts} попыток!")
           break
        elif feedback =="меньше":
            high = guess-1
        elif feedback =="больше":
            low = guess+1
        else:
            print("Можно ввести только 'меньше', 'больше' или 'угадал'!")

program_guess()