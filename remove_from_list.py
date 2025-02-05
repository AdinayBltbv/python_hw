list = ['Яблоко', 'банан', 'груша']

def remove_letter_from_list(w, l):
    return [word.replace(l.lower(), '').replace(l.upper(), '') for word in w]

remove_letter = input("Введите букву, которую нужно удалить: ")

new_list = remove_letter_from_list(list, remove_letter)
print(new_list)