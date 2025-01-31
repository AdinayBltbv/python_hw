def calculate_grades():
    grades =[]
    for i in range(10):
        grade = float(input(f'Введите оценку {i + 1}: '))
        while grade < 0 or grade > 100:
            print("Оценка должна быть от 0 до 100!")
            grade = float(input(f'Введите оценку {i + 1}: '))
        grades.append(grade)

    average = sum(grades)/ len(grades)
    print(f'Средний балл:{average}')

calculate_grades()