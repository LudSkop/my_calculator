import sys 
import pathlib


def recursive_print(path):
    if path.is_dir():
        print(path.name + '/')
        for item in path.iterdir():
            recursive_print(item)
    else:
        print(path.name)
    
def main():
   path = pathlib.Path(sys.argv[1])
   recursive_print(path)







if __name__ == "__main__":
    main()
