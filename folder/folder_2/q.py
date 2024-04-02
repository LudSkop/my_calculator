
x = 50

def test(x):
    print(f'x is {x}')
    x = 2
    print(f'changed lokal x to {x}')




test(11)
print(f'x in the end {x}')