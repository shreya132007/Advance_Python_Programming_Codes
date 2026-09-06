"""
TOPIC :- Employee Payroll Management System

Design a Python program for an Employee Payroll Management System.

CO1 – Object-Oriented Programming (10 Marks)
Create the following classes:
Employee
Data members: Employee Name, Employee ID, Basic Salary 
Constructor to initialize employee details. 
Implement a method to calculate the employee grade based on salary: 
Grade A: Salary ≥ ₹80,000 
Grade B: Salary ≥ ₹60,000 
Grade C: Salary ≥ ₹40,000 
Grade D: Salary < ₹40,000 
Implement display() and _str_() methods. 
Company
Store a list of employees. 
Implement methods to add and display employee records. 

CO2 – Dynamic Programming (10 Marks)
Implement Fibonacci using Memoization (Top-Down DP) to generate the first N Fibonacci numbers.
"""

class Employee :
    def __init__(self,Employee_Name,Employee_ID,Basic_Salary):
        self.Employee_Name=Employee_Name
        self.Employee_ID=Employee_ID
        self.Basic_Salary=Basic_Salary

    def Employee_Grade(self):
        if self.Basic_Salary >= 80000:
            return "A"
        if self.Basic_Salary >= 60000:
            return "B"
        if self.Basic_Salary >= 40000:
            return "C"
        if self.Basic_Salary < 40000:
            return "D"

    def display(self):
        print(f"Employee_ID : {self.Employee_ID}")
        print(f"Employee_Name : {self.Employee_Name}")
        print(f"Employee_Salary : {self.Basic_Salary}")
        print(f"Grade : {self.Employee_Grade()}")
        print("--------------------------")

    def __str__(self):
        return f"{self.Employee_ID}. {self.Employee_Name} has salary of Rupees {self.Basic_Salary} therefore graded as {self.Employee_Grade()}"


class Company:
    def __init__(self):
        self.Employees=[]

    def Add_Employees(self,Employee):
        self.Employees.append(Employee)
        print(f"Added Employee : {Employee.Employee_Name} (ID : {Employee.Employee_ID})")

    def display_Employees(self):
        print("Employee Payroll Records")
        print("========================")

    
e1 = Employee("Shreya",1111,70000)
print(e1)
e1.display()

e2 = Employee("Sarthak", 2222, 90000)
print(e2)
e2.display()

company = Company()

company.Add_Employees(e1)
company.Add_Employees(e2)

company.display_Employees()

print(e1)   # Using __str__() method