import random
def user_guess():
    random_num = random.randint(1,1000)
    attempts = 0
    print("Я загадала число от 1 до 1000, попробуйте его угадать!")

    while True:
        try:
            guess =int(input("Введите ваше препроложение числа: "))
            attempts +=1

            if guess < random_num:
                print("Горячо, но моё число больше!")
            elif guess > random_num:
                print("Холодно, моё число меньше!")
            else:
                print(f"Вы угадали число {random_num} за {attempts} попыток!")
                break
        except ValueError:
            print("Введите целое число")

user_guess()