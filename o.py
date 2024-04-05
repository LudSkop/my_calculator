# Порахувати суму всіх чисел чурез рекурсію.
# 10 -> 10 + 9 + 8 + 7 + 6 + 5 ..... + 1
sum = 0
# for num in range(1, 11):
#     sum += num

# print(sum)

def sum_number(max_number):
    if max_number <= 0:
        return 0
    elif max_number == 1:
        return 1
    return max_number + sum_number(max_number - 1)
print(sum_number(10))