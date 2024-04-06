# Написати функцію яка визначає чи є число простим.
from colorama import Fore

def is_prime(n:int)-> bool:
    if n <= 1:
        return False
    for i in range(2, n):
        if n % i == 0:
            return False
    return True    

def main():
    value =int(input(Fore.RED + 'Please enter the number:  ')) 
    if is_prime(value):
        print(Fore.GREEN + f'{value} - це просте число')
    else:
        print(Fore.LIGHTYELLOW_EX + f'{value} -не є простим числом')


if __name__ == "__main__":
    main()




