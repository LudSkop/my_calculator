def outer():
    x = 'local x'

    def inner():
        x = 'nonlocal x'
        print(f'inner function: {x}')


    inner()
    print(f'outer func: {x}')
outer()