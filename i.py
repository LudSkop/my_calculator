# Створити функцію яка приймає рядок  і повертає словник відповідно ASCII.
#Make func who take string and return dictionary with ASCII. 

from pprint import pprint

def anabel(string:str)-> dict:
    dic = {}
    for element in string:
        dic[element]= ord(element)
    return dic
    
    
pprint(anabel('hello world, slisa and, pusha and,'))







