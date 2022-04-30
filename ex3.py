import decorator


@decorator.decorator
def twice(func, *args, **kwargs):
    """
    Decorator that executes the given function twice.
    :param func: function to execute
    :param args: argument for the function.
    :param kwargs: dictionary for the function.
    :return: decorator.
    """
    func(*args, **kwargs)
    func(*args, **kwargs)


@twice
def add(x, y):
    return x + y


if __name__ == '__main__':
    add(5, 5)
