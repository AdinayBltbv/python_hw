def calculate():
    print("Выберите операцию: ")
    print("1: Сложение (+)")
    print("2: Вычитание (-)")
    print("3: Умножение (*)")
    print("4: Деление (/)")

    choice=input("Введите номер операции: ")

    if choice== "1":
        num1=float(input("Введите первое число: "))
        num2=float(input("Введите второе число: "))
        print(num1+num2)
    elif choice== "2":
        num1=float(input("Введите первое число: "))
        num2=float(input("Введите второе число: "))
        print(num1-num2)
    elif choice== "3":
        num1=float(input("Введите первое число: "))
        num2=float(input("Введите второе число: "))
        print(num1*num2)  
    elif choice== "4":
        num1=float(input("Введите первое число: "))
        num2=float(input("Введите второе число: "))
        if num2 !=0:
            print(num1 /num2)
        else:
            print("Делить на 0 нельзя")
    else:
        print("Такого варианта нет!")

calculate()
