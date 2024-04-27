from colorama import Fore


string ='My father usually comes home late, 2000-2024, i see everthing 78 this lesson seems interesting 1980.'

def count_digits(string):
    count = 0
    for el in string:
        if el.isdigit():
            count += 1
    return count        



print(count_digits(string))




