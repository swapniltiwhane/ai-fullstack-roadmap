# Day 3 Dictionary in Python
# Exercise 1 – Employee Profile
employee = {
    "name": "Swapnil",
    "designation": "Technical Lead",
    "experience": 15,
    "skills": ["Angular", "AWS"]
}

def display():

    for key,value in employee.items():
        if key == "name":
            print(f"Employee Name: {value}")
        elif key == "designation":
            print(f"Designation: {value}")
        elif key == "skills":
            print(f"Total Skills: {len(value)}")

def add_skills():
	new_skills = ["Python","FastAPI"]
	employee["skills"].extend(new_skills)


display()
add_skills()
display()

# Exercise 2 – Student Record
name = input("Enter Name: ")
marks = input("Enter Marks: ")
student = {}
def add_student():
	student["name"] = name
	student["marks"] = marks
add_student()
def result():
	if int(student["marks"]) >= 50:
		return "Result : Pass"
	else:
		return "Result : Fail"

print(result())

# Day 3 Dictionary in Python
# Exercise 3 – Product Inventory
products = {
    "Laptop": 10,
    "Mouse": 25,
    "Keyboard": 12
}
def display_info():
    name = input("Enter the product name: ")
    quantity = products.get(name)
    if quantity is not None:
        print(f"{name} is available with quantity: {quantity}")
    else:
        print(f"{name} is not available in the inventory.")

display_info()

# Day 3 Dictionary in Python
# Exercise 4 – Word Frequency


def word_frequency():
	sentence = input("Enter your favourite sentence: ")
	word_list = sentence.split()
	frequency = {}
	for words in word_list:
		if(words in frequency):
			frequency[words]+=1
		else:
			frequency[words] = 1
	return frequency
	
def display_frequency():
	frequency = word_frequency()
	for key, value in frequency.items():
		print(f"{key} : {value}")

display_frequency()

# Day 3 Dictionary in Python
# Exercise 5 – Personal Portfolio
portfolio = {}
print("Welcome to Personal Portfolio")
print("1. Add Portfolio")
print("2. View Portfolio")
print("3. Total Investment")
print("4. Max Investment")
print("5. Min Investment")
print("6. Category wise Investment")
print("7. Exit")

def add_portfolio():	
		category = input("Add category: ").capitalize()
		amount = int(input("Add amount: "))
		if portfolio.get(category):
			portfolio[category] +=amount
		else:
			portfolio[category] =amount

def view_portfolio():
	for category, amount in portfolio.items():
		print(f"In {category} your investment is {amount}")

def total_investment():
	total = sum(portfolio.values())
	return total

def max_investment():
	largest_category = max(portfolio, key=portfolio.get)
	largest_amount = portfolio[largest_category]
	return f"Largest Investment: {largest_category} = {largest_amount}"

def min_investment():
	smallest_category = min(portfolio, key=portfolio.get)
	smallest_amount = portfolio[smallest_category]
	return f"{smallest_category} : {smallest_amount}"

def categorywise_investment():
	print("-------- Portfolio Report --------")
	for category, amount in portfolio.items():
		print(f"{category}     :    {amount}")

def handle_empty():
	if not portfolio:
		print("Your portfolio is empty, please first add some value")
		return

def portfolio_menu():
	while True:
		try:
			option = int(input("Enter your option: "))
		except ValueError:
			print("Please enter a valid number.")
			continue
		if option != 1:
			handle_empty()
			continue
		if option == 1:
			add_portfolio()
		elif option == 2:
			view_portfolio()
		elif option == 3:
			print(f"Total Investment: {total_investment()}")
		elif option == 4:
			print(f"Max Investment: {max_investment()}")
		elif option == 5:
			print(f"Min Investment: {min_investment()}")
		elif option == 6:
			categorywise_investment()			
		elif option == 7:
			print("Exiting Portfolio Manager.")
			break
		else:
			print("Invalid option. Please try again.")

portfolio_menu()
