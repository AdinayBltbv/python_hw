# 1
try:
    a = int(input("Введите первое число: "))
    b = int(input("Введите второе число: "))
    print("Результат:", a / b)
except ZeroDivisionError:
    print("Ошибка: деление на ноль!")
except ValueError:
    print("Ошибка: введите число!")

# 2
try:
    num = int(input("Введите число: "))
    print("Вы ввели:", num)
except ValueError:
    print("Ошибка: введите число!")

# 3
try:
    f = open("text.txt", "r", encoding="utf-8")
    print(f.read())
    f.close()
except FileNotFoundError:
    print("Файл не существует!")

# 4
lst = [10, 20, 30, 40, 50]
try:
    index = int(input("Введите индекс: "))
    print("Элемент:", lst[index])
except IndexError:
    print("Ошибка: индекс вне диапазона!")

# 5
class NegativeNumberError(Exception):
    pass

try:
    n = int(input("Введите число: "))
    if n < 0:
        raise NegativeNumberError
    print("Число:", n)
except NegativeNumberError:
    print("Ошибка: число не может быть отрицательным")

# 6
try:
    x = float(input("Введите первое число: "))
    y = float(input("Введите второе число: "))
    op = input("Введите операцию (+, -, *, /): ")
    if op == "+":
        print("Результат:", x + y)
    elif op == "-":
        print("Результат:", x - y)
    elif op == "*":
        print("Результат:", x * y)
    elif op == "/":
        print("Результат:", x / y)
    else:
        print("Ошибка: неверная операция!")
except ValueError:
    print("Ошибка: введите число!")
except ZeroDivisionError:
    print("Ошибка: деление на ноль!")

# 7
try:
    f = open("data.txt", "r", encoding="utf-8")
    print(f.read())
except Exception as e:
    print("Ошибка:", e)
finally:
    try:
        f.close()
    except:
        pass

# 8
try:
    n = int(input("Введите число: "))
    if n < 0:
        raise ValueError("Отрицательное число")
    if n > 1000:
        raise OverflowError("Слишком большое число")
    print("Число:", n)
except ValueError:
    print("Ошибка: число отрицательное!")
except OverflowError:
    print("Ошибка: число слишком большое!")

# 9
try:
    a = int(input("Введите первое число: "))
    b = int(input("Введите второе число: "))
    print("Результат:", a / b)
except Exception as e:
    with open("errors.log", "a", encoding="utf-8") as log:
        log.write(str(e) + "\n")
    print("Ошибка:", e)

# 10
try:
    a = int(input("Введите первое число: "))
    b = int(input("Введите второе число: "))
    print("Результат:", a / b)
except ZeroDivisionError:
    print("Ошибка: деление на ноль!")
