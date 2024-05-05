# Сканер  тек(директорій).
from pathlib import Path



def scaner(path: Path):
    path = Path(path)
    for file_ in path.iterdir():
        if file_.is_dir():
            with open('folders.txt', mode='a', encoding='utf-8') as file:
                file.write(file_.name+ '\n')
            scaner(file_)                
        else:
            with open('files.txt', mode='a', encoding='utf-8') as file:
                file.write(file_.name+ '\n')

if __name__ == "__main__":
    scaner('folder')




