# from my_package import foo, sum, mul, log
import my_package


def mul(a):
    return a * 4

if __name__ =="__main__":
    print(my_package.foo("Alissa!!"))
    print(my_package.sum(10, 50))
    print(my_package.mul(2, 8))
    my_package.log("My happy birthday")
    print(my_package.a())
    print(mul(5))
