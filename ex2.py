def surprise_decorator(func):
    """
    Decorator that print surprise instead of the original functionality of the given function.
    :param func: function to execute.
    :return: decorator.
    """
    def inner(*args):
        print("Surprise")
    return inner


@surprise_decorator
def sqrt(num):
    return num**2


if __name__ == '__main__':
    sqrt(8)
