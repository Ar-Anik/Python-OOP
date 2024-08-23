def public_function():
    print("This is a public function.")

def _protected_function():
    print("This is a protected function.")

def __private_function():
    print("This is a private function")

class PublicClass:
    def public_method(self):
        print("This is a public method from PublicClass.")

    def _protected_method(self):
        print("This is a protected method from PublicClass.")

    def __private_method(self):
        print("This is a private function from PublicClass.")

# obj1 = PublicClass()
# obj1._private_method()