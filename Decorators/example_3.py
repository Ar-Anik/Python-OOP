def memorize(method):
    cache = {}

    def wrapper(*args):
        if args in cache:
            print(f"Cache hit for {method.__name__}({args})")
            return cache[args]
        else:
            print(f"Save result for {args}")
            result = method(*args)
            cache[args] = result
            return result

    return wrapper

@memorize
def fibonacci(n):
    if n <= 1:
        return n

    return fibonacci(n-1) + fibonacci(n-2)

print(fibonacci(20))
print(fibonacci(10))
print(fibonacci(20))
