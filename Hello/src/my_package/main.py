# from my_package import foo, sum, mul, log
import my_package


def mul(a):
    return a * 4


print(my_package.foo("Alissa!!"))
print(my_package.sum(10, 50))
print(my_package.mul(2, 8))
my_package.log("My happy birthday")
print(my_package.infa_foo())
print(mul(5))
