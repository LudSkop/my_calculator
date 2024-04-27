from colorama import Fore


string ='My father usually comes home late, 2000-2024, i see everthing 78 this lesson seems interesting 1980.'

def count_number(string):
    count = 0
    position = 0
    nums = []
    while position < len(string):
        if string[position].isdigit():
            num =''
            while position < len(string) and string[position].isdigit():
                num += string[position]
                position +=1
            nums.append(num)
            count += 1
        else:
            position += 1
    return count, nums      


print(count_number(string))
