#
# Decorators/time.py
# Decrypt
#
# Written by Firsov Georgy
# Copyright © 2019 Firsov Georgy. All rights reserved.
#


def benchmark(entire):
    """Decorator to measure execution time

    :param entire: wrapped function to benchmark
    """

    from datetime import datetime

    def wrapper(*args, **kwargs):
        start = datetime.now()
        result = entire(*args, **kwargs)
        end = datetime.now()

        diff = end - start

        print("Time elapsed: {}".format(diff))

        return result

    return wrapper
