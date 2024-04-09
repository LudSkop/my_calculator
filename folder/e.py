
ankor = 'He wants to do it right now.'
number_dict = {}

for char in ankor:
    try:
        count = number_dict[char]
    except KeyError:
        count = 0

    count += 1
    number_dict[char] = count




print(number_dict)






