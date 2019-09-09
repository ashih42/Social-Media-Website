from functools import wraps

def logme(func):
    import logging
    logging.basicConfig(level=logging.DEBUG)

    @wraps(func)
    def inner(*args, **kwargs):
        logging.debug('Called {} with args {} and kwargs {}'.format(
            func.__name__,
            args,
            kwargs))
        return func(*args, **kwargs)
    return inner

@logme
def print_2():
    print(2)

@logme
def print_stooges(x, y, z='Moe'):
    ''' Print out the 3 stooges '''
    print('Stooges: {}, {}, {}'.format(x, y, z))





























