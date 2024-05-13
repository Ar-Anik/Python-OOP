import time

def measure_time(method):
    def wrapper(*args, **kwargs):
        print("Argument : ", args)
        print("Keyword Argument : ", kwargs)
        start_time = time.time()
        result = method(*args, **kwargs)
        end_time = time.time()
        execute_time = end_time - start_time
        print(f"Execution time for {method.__name__}: {execute_time} seconds.")
        return result
    return wrapper

@measure_time
def count_time(n):
    for _ in range(n):
        pass

count_time(100000000)
