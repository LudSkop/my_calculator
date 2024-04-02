
x = 50

def test():
    global x
    print(f'x is {x}')
    x = 2
    print(f'changed lokal x to {x}')




test()
print(f'x in the end {x}')