from functools import wraps


class MyClass:
    def __init__(self, name):
        self.my_name = name

    @property
    def name(self):
        return self.my_name

    @staticmethod
    def say_hi():
        print("Hi")


def my_decorator(func):
    @wraps(func)
    def inner(*args):
        return func(args)
    return inner


def add(x, y):
    """
    Add two number and return the result.
    :param x: first integer
    :param y: second integer
    :return: x + y
    """
    return x + y


if __name__ == '__main__':

    print(my_decorator(add).__doc__)  # The documentation of inner is the same doc like add function.
    print(add.__doc__)
    MyClass.say_hi()  # static method

    my_class = MyClass("Dvir") # property
    my_class.name = "d"


