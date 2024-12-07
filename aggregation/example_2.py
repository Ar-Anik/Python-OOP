class Country:
    def __init__(self, name, population=0):
        self.name = name
        self.population = population

    def country_info(self):
        return f"Name : {self.name}, Total Population : {self.population}"

class Person:
    def __init__(self, name, country):
        self.name = name
        self.country = country

    def person_info(self):
        return f"Name : {self.name}, \nCountry {self.country.country_info()}"


country = Country("Bangladesh", 120)
person = Person("Anik", country)
print(person.person_info())

# After delete container
del person
print(country.country_info())

