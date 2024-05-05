




# def factorial(n):
#     if n < 2:
#         return 1
#     else:
#         return n * factorial(n - 1)
    
# def number_of_groups(n, k):
#     a = factorial(n)
#     b = factorial(n - 1)
#     c = factorial(k)
#     return int(a // b * c)



# print(factorial(7))
# print(number_of_groups(10, 4))

from pathlib import Path


current_dir = Path('.')

#file = current_dir / 'folder_2'/ 'folder_3'/'e.py'
file = current_dir/'e.py'
print(file.exists())



