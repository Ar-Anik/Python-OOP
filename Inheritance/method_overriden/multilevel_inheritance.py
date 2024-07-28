class Father:
    def write(self):
        print("Called From Father")

class Son(Father):
    def write(self):
        print("Called From Son")

class Grandson(Son):
    def write(self):
        print("Called From Grand-Child")

obj = Grandson()
obj.write()

Son.write(obj)
Father.write(obj)
