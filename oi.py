#Потрібно створити список в якому будуть лише цифри із строки.

offer = 'ae26j70k3678dgfgghr65776787dvsdgfhfert569#!6'

number = []
 
for el in offer:
    if '0'<= el <= '9':
       number.append(el)


number_set = set(number)    






print(number)
print(type(number_set))
print(number_set)