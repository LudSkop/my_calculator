# Створити функцію яка приймає рядок  і повертає словник відповідно ASCII.
#Make func who take string and return dictionary with ASCII. 

from pprint import pprint
from colorama import Fore

def anabel(string:str)-> dict:
    dic = {}
    for element in string:
        if  not element in dic:
            dic[element]= ord(element)
    return dic
    
    
pprint(anabel(Fore.RED + 'hello world, slisa and, pusha and,'))







