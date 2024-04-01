def  pay_payment(params_1,  *args , **kwargs):
    print(params_1)
    print( args)
    print(type(args))
    print(kwargs)
    print(type(kwargs))
    
   
    





res = pay_payment(167, 37,53,7, 4, 7, s=234, liuda=200, vlad= 2000, oleg= 1000,   )
print(res)