# Порахувати суму всіх аргументів
def sum(start, *args):
    sum = start
    for element in args:
        sum += element
    return sum
    

result = sum( 5, 5, 5, 5, 1, 12)
print(result)








