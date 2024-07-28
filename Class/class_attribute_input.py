class Information:
    university = "UAP"

    def __init__(self, name, id, department):
        self.name = name
        self.id = id
        self.department = department

    def write(self):
        print("Name : ", self.name)
        print("ID : ", self.id)
        print("Department : ", self.department)

std = Information(input("Name : "), input("ID : "), input("Department : "))
std.id = "181010" + std.id
std.write()
