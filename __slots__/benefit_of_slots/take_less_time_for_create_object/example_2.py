"""
timeit() function is part of Python's timeit module, which is designed to measure the execution time of small code snippets with high precision. It is commonly used for comparing the performance
of different implementations.
"""

from timeit import timeit

class WithOutSlots:
    pass

class WithSlots:
    __slots__ = ('name', 'age', 'university')

def with_out_slots():
    obj = WithOutSlots()
    obj.name = 'Anik'
    obj.age = 14
    obj.university = "UAP"

def with_slots():
    obj = WithSlots()
    obj.name = "Anik"
    obj.age = 14
    obj.university = "UAP"

num_instance = 10000000

# globals() function is used to pass the current global scope, This allows the code (the stmt argument) to access variables, functions, or objects that are defined outside the immediate string that timeit() is executing.
time_without_slots = timeit("with_out_slots()", globals=globals(), number=num_instance)
print(f"Time for creating and initializing objects Without Slot : {time_without_slots:.4f} seconds.")

time_with_slots = timeit("with_slots()", globals=globals(), number=num_instance)
print(f"Time for creating and initializing objects With Slot : {time_with_slots:.4f} seconds.")


"""
Signature of timeit():
        timeit(stmt='pass', setup='pass', timer=<default timer>, number=1000000, globals=None)

Parameters :
1. stmt (required): This is the code snippet (a string or callable) that we want to run. It defaults to 'pass', which means it does nothing. In your example, the stmt is "with_out_slots()", 
which calls the with_out_slots() function.

2. setup (optional): This is a string or callable that contains setup code that is executed once before the stmt. This is useful for preparing the environment or initializing objects. It defaults to 'pass'.
For example, if we need to import modules or create objects before the timed statement runs, we would include that here. In our case, don't need setup because all necessary variables and functions are already 
available.

3. timer (optional): This specifies the timer function to use. The default is platform-dependent:
    # On Windows, it uses time.perf_counter().
    # On Unix systems, it uses time.process_time().
Typically, don't need to provide this unless we're implementing a custom timer.

4. number (optional): This is the number of times stmt is executed. It defaults to 1,000,000 if not specified.
In our case, number=1000000 means the with_out_slots() function is called 1,000,000 times to measure the total time.

5. globals (optional): This allows us to pass the global variables into the timeit() function so that the stmt can access the functions, variables, and objects that define in our script.
By passing globals=globals(), the function can reference with_out_slots() and with_slots() without any issues.

Return Value: The function returns the total execution time (in seconds) it took to execute the stmt number times. The time is measured as a floating-point value.

globals() function : globals() is a built-in Python function that returns a dictionary representing the global symbol table (i.e., all the global variables and functions defined in the current module or script).
This dictionary contains all global identifiers (variable names, function names, etc.) and their corresponding values in the current scope.

"""