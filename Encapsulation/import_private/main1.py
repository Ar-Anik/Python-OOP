import my_module

if __name__ == "__main__":

    my_module.public_function()

    try:
        my_module._private_function()
    except AttributeError:
        print("Cannot access _private_function from outside my_module.")

    my_object = my_module.PublicClass()

    try:
        my_object._private_method()
    except AttributeError:
        print("Cannot access _private_method from outside PublicClass instance.")
