from functools import wraps


def type_check(correct_type):
    """
    Decorator that check if the given function received correct type of argument.
    :param correct_type: The type of the argument.
    :return: decorator
    """
    def check(func):
        @wraps(func)
        def inner(arg):
            if isinstance(arg, correct_type):
                return func(arg)
            raise ValueError("Argument type is incorrect")
        return inner
    return check


@type_check(int)
def times2(num):
    return num*2


if __name__ == '__main__':
    print(times2(5))
    print(times2("5"))
