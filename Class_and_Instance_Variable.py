# class variable is universal, instance variable is object dependent.

class Worker:
    company = "Divine IT Limited"           # class variable

    def __init__(self, name, id, salary):
        self.name = name                    # instance variable
        self.id = id                        # instance variable
        self.salary = salary                # instance variable

    def write(self):
        print("{}--{}--{}--{}".format(self.name, self.company, self.id, self.salary))

wrkr = Worker("Anik", "22209", 10000)
wrkr.write()

# instance variable change
wrkr.name = "Montu"
print("Name : ", wrkr.name)

Worker.name = "O"                       # it create new attribute of Worker class
print(wrkr.name)

# class variable change
Worker.company = "BrainBlog IT Limited"
wrkr.write()

#if we change class variable by object it not change orginal class variable
wrkr.company = "Brain Fuck"
print(Worker.company)
wrkr.write()
