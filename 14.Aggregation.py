# Employee class — independent
class Employee:
    def __init__(self, name):
        self.name = name

    def show_info(self):
        print(f"Employee Name: {self.name}")


# Department class — uses Employee via aggregation
class Department:
    def __init__(self, dept_name, employee):
        self.dept_name = dept_name
        self.employee = employee  # 🔁 Aggregation (reference passed)

    def show_department(self):
        print(f"Department: {self.dept_name}")
        self.employee.show_info()


# Independent employee
e1 = Employee("Ali")

# Department using employee (aggregation)
d1 = Department("HR", e1)

# Show department info
d1.show_department()

# Delete department
del d1

# Employee still usable
e1.show_info()
