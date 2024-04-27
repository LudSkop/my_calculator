string = 'Hello world [my love], and [i like it] do they often discuss it. '

# start_index = string.find('[')
# end_index = string.find(']')

# new_string = string[:start_index] + string[end_index + 1]


# print(new_string)

def sanitize(sting):
    new_string = string[:]
    while True:
        start_index = new_string.find('[')
        end_index = new_string.find(']')
        if start_index == -1:
            break
        new_string = new_string[:start_index] + new_string[end_index +1 :]
    return new_string


print(sanitize(string))





