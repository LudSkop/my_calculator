from colorama import Fore


string = 'Hello world [my love], and [i like it] do they often discuss it. '


def sanitize(sting):
    new_string = string[:]
    while True:
        start_index = new_string.find('[')
        end_index = new_string.find(']')
        if start_index == -1:
            break
        new_string = new_string[:start_index] + new_string[end_index +1 :]
    return new_string


print(Fore.LIGHTRED_EX + sanitize( string))





