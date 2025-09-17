def calculator():
    x = float(input("Введите первое число: "))
    y = float(input("Введите второе число: "))
    operation = input("Выберите операцию (+ или -): ")

    if operation == "+":
        result = x + y
    elif operation == "-":
        result = x - y
    else:
        print("Неверная операция")
        return

    print("Результат:", result)

calculator()