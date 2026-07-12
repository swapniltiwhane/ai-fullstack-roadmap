# function in python
def printName(name="swapnil", greeting="Hello"):
    return f"{greeting} {name}'s"

print(printName(greeting="Namaste", name="Prachi"));
# Add 2 numbers
def addNumbers(num1, num2):
    return num1 + num2
num1=int(input("Enter 1st number: "))
num2=int(input("Enter 2nd number: "))
print(f"Number 1 {num1} and number 2 {num2} is {addNumbers(num1, num2)}")
# Find the largest of two numbers
def largestNumber(num1, num2):
    if num1 > num2:
        return num1
    else:
        return num2
print(f"The largest number between {num1} and {num2} is \n {largestNumber(num1, num2)}")
#Check even/odd
def checkEvenOdd(num):
    if num % 2 == 0:
        return "Even"
    else:
        return "Odd"
print(f"The number {num1} is {checkEvenOdd(num1)}")
print(f"The number {num2} is {checkEvenOdd(num2)}")

# Employee salary calculation
empname = input("Enter name: ")
salary = int(input("Enter salary: "))
def caculateHRA(salary):
    return salary * 0.2  # HRA is 20% of salary
def calculatePF(salary):
    return salary * 0.12  # PF is 12% of salary
def calculateTax(salary):
    return salary * 0.1  # Tax is 10% of salary
def calculateNetSalary(salary):
    hra = caculateHRA(salary)
    pf = calculatePF(salary)
    tax = calculateTax(salary)
    net_salary = salary - (hra + pf + tax)
    return net_salary
def calculateSalary(empname, salary):
    # calculate HRA, PF, tax, and net salary
    hra = caculateHRA(salary)
    pf = calculatePF(salary)
    tax = calculateTax(salary)
    net_salary = calculateNetSalary(salary)
    return f"Employee Name: {empname}\nSalary: {salary}\nHRA: {hra}\nPF: {pf}\nTax: {tax}\nNet Salary: {net_salary}"
print(calculateSalary(empname, salary), end=" ")