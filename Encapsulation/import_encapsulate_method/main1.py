import my_module

if __name__ == "__main__":

    my_module.public_function()

    try:
        my_module._protected_function()
        my_module.__private_function()
    except AttributeError:
        print("Cannot access _private_function from outside my_module.")

    my_object = my_module.PublicClass()

    try
        my_object.public_method()
        my_object._protected_method()
        my_object.__private_method()
    except AttributeError:
        print("Cannot access _private_method from outside PublicClass instance.")
