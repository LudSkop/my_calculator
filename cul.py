def bubble_sort(some_list):
    length_list = len(some_list)

    for count in range(length_list-1):
        for index in range(length_list - 1 - count):
            if some_list[index] > some_list[index + 1]:
                some_list[index],some_list[index + 1] = some_list[index + 1], some_list[index]
    return some_list


if __name__ == "__main__":
    a = [10, 5, 2, 0, -4, 3, 3, 7,] 
    b = [-2, -7, 7, -2, -3]   
    print(bubble_sort(b))
