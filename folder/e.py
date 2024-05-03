# Читаємо файл за допомогою бібліотеки pathlib.

from pathlib import Path


folders = Path('./folder_2')
file_name = folders /'step.py'


try:

    with open(file_name, 'r', encoding='utf-8') as file:
        for line in file:
            print(line, end='')
except OSError as error:
    print(f'Error is : {error}')
finally:
    print('/n file read complete')









