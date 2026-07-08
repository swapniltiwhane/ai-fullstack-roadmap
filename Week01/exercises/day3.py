#Ask user queries and display output
age = int(input("Enter your age:"));
tech = input("Enter your technology, most preference only");
exp = int(input("Enter your programming experience"));
python = bool(input("do you know python? (yes/no)"));
js = bool(input("do you know javascript? (yes/no)"));
if exp < 2 and age >80 and js:
    print("You are too old to learn programming");
elif exp > 10 and age >30 and age < 40 and python:
    print("You have golden peak in your life");
elif exp > 10 and age >40 and python:
    print("Your experience is your weapon, welcome to AI world");
else:
    print("You are in the right track, keep learning and exploring new things");

# if elif statement , Comparison operator, logical operator, nested conditions, and boolean values
#Exercise 1: Event or odd
input_number = int(input("Enter number: "));
print("Even" if input_number % 2 == 0 else "Odd");
#Excercise 2:Largest number
num1 = input_number;
num2 = int(input("Enter second number"));
num3 = int(input("Enter third number"));
if num1 > num2 and num1> num3:
    print(f"Largest number {num1}");
elif num2 > num1 and num2 >  num3:
    print(f"Largest number {num2}");   
else:
    print(f"Largest number {num3}");

#Calculate grade
grade = int(input("Enter your marks"));

if grade >=90:
    print("Congratulation! You have A Grade");
elif grade >=80:
    print("You have B Grade");
elif grade >=70:
    print("You have C Grade");
elif grade >=60:
    print("You have D Grade");
else:
    print("You have F Grade");

