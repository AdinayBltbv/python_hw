# task 1
for i in range(1,11):
    print(f"{i} * {i} = {i*i}")

# task 2
for i in range(1,11):
    for y in range(1,11):
        print(f"{i} * {y} = {i * y}")
    print("-" * 10)

# task 3
def vowels_count(i):
    vowels="AEUOIaeoiu"
    return sum(1 for char in i if char in vowels)

text_input =input("Введите текст: ")
print("Количество гласных: ",vowels_count(text_input))

# task 3
list = [12345,34565,276852,1234,1,3,4,5,6]
max=list[0]
min=list[0]

for num in list:
    if num> max:
        max=num
    if num< min:
        min=num


print("Max: ", max)
print("Min: ", min)