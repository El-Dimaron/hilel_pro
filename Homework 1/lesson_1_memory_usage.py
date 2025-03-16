import os
import tracemalloc
import psutil
import functools


############
# OPTION 1 #
############

def memory_usage_tracemalloc(f):
    """Indicates the Memory Usage bytes"""
    @functools.wraps(f)
    def inner(*args, **kwargs):
        tracemalloc.start()
        result = f(*args, **kwargs)
        current, peak = tracemalloc.get_traced_memory()
        tracemalloc.stop()
        print(f"Current memory on '{f.__name__}': {current} B.\nPeak memory on '{f.__name__}': {peak} B.")
        return result

    return inner


############
# OPTION 2 #
############

def process_memory():
    """Indicates current memory in bytes (intermediate function)"""
    process = psutil.Process(os.getpid())
    mem_info = process.memory_info()
    return mem_info.rss


def memory_usage_psutil(f):
    """Indicates the Memory Usage bytes"""
    @functools.wraps(f)
    def inner(*args, **kwargs):
        memory_start = process_memory()
        result = f(*args, **kwargs)
        memory_end = process_memory()
        print(f"Memory used on '{f.__name__}': {memory_end - memory_start} B")
        return result
    return inner


#############
# CPU USAGE #
#############

def cpu_usage(f):
    """ Indicates the CPU utilization in %"""
    @functools.wraps(f)
    def inner(*args, **kwargs):
        start = psutil.cpu_percent()
        result = f(*args, **kwargs)
        end = psutil.cpu_percent()
        print(f"CPU percent on '{f.__name__}': {end - start} %")
        return result

    return inner


##########################
# Basic status indicator #
##########################

def status(f):
    @functools.wraps(f)
    def inner(*args, **kwargs):
        print(f"The function '{f.__name__}' is being executed.")
        result = f(*args, **kwargs)
        print(f"The function '{f.__name__}' is finished.")
        return result

    return inner


@memory_usage_tracemalloc
@memory_usage_psutil
@cpu_usage
@status
def test_func():
    test_list = [x for x in range(50000)]
    return test_list


if __name__ == "__main__":
    test_func()
