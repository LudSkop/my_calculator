x = 50 #global scope
def outer():
    x = 'local x'#enclosed scope

    def inner():
        nonlocal x
        x = 'nonlocal x'#local scope
        print(f'inner function: {x}')


    inner()
    print(f'outer func: {x}')
outer()