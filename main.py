from colorama import Fore


def main(result=None, operator=None, operand=None, wait_for_number=True):
 
    while True:
        user_input = input(Fore.GREEN + '>>>>:   ')
        user_input = user_input.strip()
        if user_input == '=':
            break

        if wait_for_number:
            try:
                operand =float(user_input)
            except ValueError:
                print(Fore.LIGHTRED_EX + f'{user_input} is not a namber')
                continue
            wait_for_number = False
            if result is None:
                result = operand
            else:
                if operator == '+':
                    result += operand
                elif operator == '-':
                    result -= operand
                elif operator == '*':
                    result *= operand
                elif operator == '/':
                    if operand == 0:
                        print(Fore.BLACK + 'Devision by zero')
                        continue
                    result /= operand
        else:
            if user_input in '+-*/':
                operator = user_input
            else:
                operator = None
            if operator is None:
                print(Fore.CYAN + f"{user_input} is not '+' '-' '*' '/' ")
            else:
                wait_for_number = True    
    print(Fore.LIGHTMAGENTA_EX + str(result))



if __name__ == "__main__":
    main()







