class Father1(object):
    def write(self):
        print("Called From Father 1")

class Father2(object):
    def write(self):
        print("Called From Father 2")

class Father3(object):
    def write(self):
        print("Called From Fahter 3")

class Child(Father1, Father2, Father3):
    def write(self):
        Father1.write(self)
        Father2.write(self)
        Father3.write(self)

obj1 = Child()
obj1.write()
