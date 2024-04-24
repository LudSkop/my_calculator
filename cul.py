from pathlib import Path
import sys 


p = Path(sys.argv[1])
def  parse_folder(path:Path): 
    for el in path.iterdir():
        if el.is_dir():
            print(f'parse_folder: this is folder {el.name}') 
        else:
            print(f'parse_folder: this is file {el.name}')


if __name__ == "__main__":
    parse_folder(p)