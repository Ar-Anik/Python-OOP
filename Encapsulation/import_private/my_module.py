def public_function():
    print("This is a public function.")

def _private_function():
    print("This is a private function.")

class PublicClass:
    def public_method(self):
        print("This is a public method from PublicClass.")

    def _private_method(self):
        print("This is a private method from PublicClass.")

# obj1 = PublicClass()
# obj1._private_method()