# Задача 1. Создание и запись данных в файл
with open("data.txt", "w", encoding="utf-8") as file:
    file.write("Привет, мир!")
print("#1 выполнена — файл создан и записан текст.")


# Задача 2. Чтение содержимого файла
with open("data.txt", "r", encoding="utf-8") as file:
    content = file.read()
print("Содержимое файла data.txt:")
print(content)


# Задача 3. Добавление текста в конец файла
with open("data.txt", "a", encoding="utf-8") as file:
    file.write("Учиться программировать — это весело!")
print("Задача 3 выполнена — добавлен текст в конец файла.")


# Задача 4. Подсчёт количества строк в файле
with open("data.txt", "r", encoding="utf-8") as file:
    lines = file.readlines()
print(f"Количество строк в файле data.txt: {len(lines)}")


# Задача 5. Работа с библиотекой os
import os
if os.path.exists("data.txt"):
    print("Файл найден")
else:
    print("Файл не найден")


# Задача 6. Работа с библиотекой json
import json
user_data = {"name": "Алина", "age": 21}
with open("user.json", "w", encoding="utf-8") as file:
    json.dump(user_data, file, ensure_ascii=False, indent=4)
print("Задача 6 выполнена — файл user.json создан.")


# Задача 7. Чтение данных из JSON-файла
with open("user.json", "r", encoding="utf-8") as file:
    data = json.load(file)
print(f"Имя пользователя: {data['name']}")


# Задача 8. Работа с библиотекой csv
import csv
with open("students.csv", "w", newline="", encoding="utf-8") as file:
    writer = csv.writer(file)
    writer.writerow(["Имя", "Возраст"])
    writer.writerow(["Анна", 20])
    writer.writerow(["Иван", 22])
    writer.writerow(["Марат", 19])
print("Задача 8 выполнена — файл students.csv создан.")


# Задача 9. Чтение CSV-файла
with open("students.csv", "r", encoding="utf-8") as file:
    reader = csv.DictReader(file)
    print("Студенты старше 20 лет:")
    for row in reader:
        if int(row["Возраст"]) > 20:
            print(f"{row['Имя']} — {row['Возраст']} лет")


# Задача 10. Использование библиотеки shutil
import shutil
shutil.copy("data.txt", "backup.txt")
print("Задача 10 выполнена — файл data.txt скопирован в backup.txt.")
