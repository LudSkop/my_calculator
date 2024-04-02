def outer():
    x = 'local x'

    def inner():
        nonlocal x
        x = 'nonlocal x'
        print(f'inner function: {x}')


    inner()
    print(f'outer func: {x}')
outer()