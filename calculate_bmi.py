def calculate_bmi(weight, height):
    bmi = weight / (height ** 2)
    if bmi < 18.5:
        category = "Худой(ая)"
    elif 18.5 <= bmi < 24.9:
        category = "Норма"
    elif 25 <= bmi < 29.9:
        category = "Избыточный вес"
    else:
        category = "Ожирение"
    return bmi, category

weight = float(input("Введите ваш вес (кг): "))
height = float(input("Введите ваш рост (м): "))

bmi, category = calculate_bmi(weight, height)
print(f"Ваш BMI: {bmi}. Категория: {category}")
