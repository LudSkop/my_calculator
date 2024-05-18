from my_package import module_b


def dudu():
    print("from dudu module_a")


if __name__ == "__main__":
    dudu()
    module_b.thing()
