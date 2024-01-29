class Employee:
    def __init__(self, employee_id, name, age, salary):
        self.employee_id = employee_id
        self.name = name
        self.age = age
        self.salary = salary

    def __str__(self):
        return f"{self.employee_id:<10}{self.name:<15}{self.age:<10}{self.salary:<10}"

class EmployeeComparator:
    def __init__(self, sorting_parameter):
        self.sorting_parameter = sorting_parameter

    def compare(self, emp1, emp2):
        if self.sorting_parameter == 1:
            return emp1.age - emp2.age
        elif self.sorting_parameter == 2:
            return cmp(emp1.name, emp2.name)
        elif self.sorting_parameter == 3:
            return emp1.salary - emp2.salary
        else:
            raise ValueError("Invalid sorting parameter")

def main():
    employees = [
        Employee("161E90", "Ramu", 35, 59000),
        Employee("171E22", "Tejas", 30, 82100),
        Employee("171G55", "Abhi", 25, 100000),
        Employee("152K46", "Jaya", 32, 85000)
    ]
    print("Choose sorting parameter:")
    print("1. Age")
    print("2. Name")
    print("3. Salary")
    sorting_parameter = int(input())

    employees.sort(key=lambda emp: getattr(emp, ['age', 'name', 'salary'][sorting_parameter - 1]))
    
    print(f"{'Employee ID':<10}{'Name':<15}{'Age':<10}{'Salary':<10}")
    print("-------------------------------------------")
    for employee in employees:
        print(employee)


if __name__ == "__main__":
    main()
