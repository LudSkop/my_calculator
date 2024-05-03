# Основні можливості pathlib.
from pathlib import Path


current_path = Path()
print(current_path)
print(current_path.cwd)
file = current_path/'folder_2'/'folder_3'/'e.py'
print(file)
file = current_path.joinpath('folder_2','folder_3','e.py')
print(file)
print(file.parts)
print(file.name)
print(file.parent)
print(file.suffix)
print(file.suffixes)








