def calculator():
    print("Выберите операцию:")
    print("1: Сложение (+)")
    print("2: Вычитание (-)")
    print("3: Умножение (*)")
    print("4: Деление (/)")

    choice = input("Введите число операции: ")

    if choice not in ['1', '2', '3', '4']:
        print("Неверный выбор операции.")
        return

    try:
        num1 = float(input("Введите 1ое число: "))
        num2 = float(input("Введите 2ое число: "))
    except ValueError:
        print("Ошибка, введите числа.")
        return

    if choice == '1':
        print(f"Результат: {num1} + {num2} = {num1 + num2}")
    elif choice == '2':
        print(f"Результат: {num1} - {num2} = {num1 - num2}")
    elif choice == '3':
        print(f"Результат: {num1} * {num2} = {num1 * num2}")
    elif choice == '4':
        if num2 == 0:
            print("Ошибка: Деление на ноль невозможно.")
        else:
            print(f"Результат: {num1} / {num2} = {num1 / num2}")

calculator()
