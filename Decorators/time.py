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

        print("Time elapsed: {} sec, {} msec".format(diff.seconds, diff.microseconds))

        return result

    return wrapper
