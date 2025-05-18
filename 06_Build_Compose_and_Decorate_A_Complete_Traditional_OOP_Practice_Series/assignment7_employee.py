"""Create a class Employee with:

a public variable name,

a protected variable _salary, and

a private variable __ssn.

Try accessing all three variables from an object of the class and document what happens."""


class Employee:
    def __init__(self, name, salary, ssn):
        self.name = name              # Public
        self._salary = salary         # Protected
        self.__ssn = ssn              # Private

emp = Employee("Ali", 50000, "123-45-6789")
print(emp.name)         # Accessible
print(emp._salary)      # Accessible but discouraged
# print(emp.__ssn)      # Will raise AttributeError
print(emp._Employee__ssn)  # Access private using name mangling(Name mangling is a way Python protects class-private variables from being accidentally accessed or changed.)
