import time
from functools import wraps

def timethis(function):
    """
    Python decorator to profile function execution time using built in
    time module from python. This function decorator times the execution
    of wrapped fucntion and logs to the terminal.
    """

    @wraps(function)
    def wrapper(*args, **kwargs):
        # Start timing the function
        start = time.perf_counter()
        r = function(*args, **kwargs)
        end = time.perf_counter()

        print('{}.{} : {}s'.format(function.__module__, function.__name__, end - start))
        return r
    return wrapper
