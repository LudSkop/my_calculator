# Написати функцію яка визначає чи є число простим.
from colorama import Fore
from tabulate import tabulate

        
def is_prime(n:int)-> bool:
    if n <= 1:
        return False
    for i in range(2, n):
        if n % i == 0:
            return False
    return True    

def main()-> dict[str:list]:
    data = {}
    data['prime'] = []
    data['composite'] = []
    while True:
        try:
            value =int(input(Fore.RED + 'Please enter the number:  ')) 
            if is_prime(value):
                print(Fore.GREEN + f'{value} - це просте число')
                data['prime'].append(value)
            else:   
                print(Fore.LIGHTYELLOW_EX + f'{value} -не є простим числом')
                data['composite'].append(value)
        except ValueError:
            ...
        
        if value == 6:
            break
    return data    


if __name__ == "__main__":
   
    tab = tabulate(main(), headers='keys', tablefmt='grid')
    print(Fore.LIGHTBLUE_EX + tab)




