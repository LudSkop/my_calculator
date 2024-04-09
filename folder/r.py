from random import randint
from colorama import Fore
from tabulate import tabulate


def name(n:int)-> int:
    count = 0
    qote = randint(0, n)
    result = {'число більше': [], 'число меньше': [], 'вгадане число': []}
    while True:
        try:
            answer = int(input(Fore.LIGHTBLUE_EX + f'Вгадай задумане число від 0 до {n}: '))
            count = count + 1
        except Exception:
            print("It's not number") 
        if answer > qote:
            print(Fore.LIGHTGREEN_EX + 'Ваше число більше за задумaне .')
            result["число більше"].append(answer) 
        elif answer < qote:
            print(Fore.LIGHTYELLOW_EX + 'Ваше число меньше за задумане .')
            result['число меньше'].append(answer)
        else:
            print(Fore.RED + f'Ви вгадали число за таку кількість кроків :{count}')
            result['вгадане число'].append(answer)
            break
    return result
   

rez = tabulate(name(6), headers='keys',  tablefmt='grid', )
print(rez)








