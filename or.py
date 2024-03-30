import sys 
import pathlib


def recursive_ptint(path):
    if path is dir():
        print(path.name() + '/')
    else:
        print(path.name)
    for item in path.iterdir():
        recursive_ptint(item)
def main():
   path = pathlib.Path(sys.argv[1])
   recursive_ptint(path)







if __name__ == "__main__":
    main()
