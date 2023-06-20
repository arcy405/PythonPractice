class Employee:
    def __init__(self, name, salary):
        self.name = name
        self.salary = salary

    # salary = 200000
    # name = "Archan aPAnt"
    def getSalary(self):
        print(self.salary)


rohan = Employee("Rohan Sharma", "2000")

print(rohan.salary)
print(rohan.name)
# rohan.getSalary()
#
harry = Employee("Harry Sharma", "777000")

print(harry.salary)
print(harry.name)
harry.getSalary()
rohan.getSalary()
