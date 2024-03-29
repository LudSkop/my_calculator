from oi import get_name

def goodbuy(name):
    print(f'Goodbuy {name} ')

def main():
    name = get_name()
    goodbuy(name)


if __name__ == "__main__":
    print(f'__name__ == { __name__}')
    main()



