# Знайти в строці підстроку.

main_string = input('Введіть строку: ')
sub_string = input('Введіть підстроку для пошуку: ')
index_string = main_string.find(sub_string)
if index_string != -1:
    print(f'Знайдена підстрока в строці за таким індексом: {index_string}')
else:
    print(f'Підстрока не знайдена')











