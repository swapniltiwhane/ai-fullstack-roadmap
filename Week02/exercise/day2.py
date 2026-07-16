#List in Python

# Exercise 1 – Favorite Technologies
technologies = []
def add_technology(tech):
	technologies.append(tech)

def main():
    while True:
        user_technology = input("Add your favourite technology (or type 'exit' to finish): ")
        if user_technology.lower() == 'exit':
            break
        if user_technology.lower() in [tech.lower() for tech in technologies]:
            print(f"{user_technology} is already in the list.")
            continue
        add_technology(user_technology)
       # print(f"Current list of technologies: {technologies}")
    print("Final list of favorite technologies:", technologies)
    print(f"Total Technologies added: {len(technologies)}")
main()

#List in Python

# Exercise 2 – Student Marks
marks = []

def add_mark(mark):
	marks.append(mark)

def max_marks():
	if len(marks):
		sorted_marks = sorted(marks, reverse=True)
		return sorted_marks[0]
	else:
		return 0
def min_marks():
	if len(marks):
		sorted_marks = sorted(marks)
		return sorted_marks[0]
	else:
		return 0
def avg_marks():
	marks_count = len(marks)
	if len(marks):
		return round(sum(marks)/marks_count, 2)
	else:
		return 0
	
def student_marks():
	while True:
		user_selection = input("Add marks you want to enter or type Exit to end:")
		if(user_selection == 'Exit'):
			break
		else:
			add_mark(float(user_selection))
	print(f"Your Maximum marks are {max_marks()}")
	print(f"Your Minimum marks are {min_marks()}")
	print(f"Your Average marks are {avg_marks()}")
	
student_marks()

#List in Python

# Exercise 3 – Remove Duplicates
numbers = [1,2,2,3,4,4,5]
unique_numbers = []

def add_number(number):
	unique_numbers.append(number)

def check_unique_number(number):
	if number not in unique_numbers:
		add_number(number)
	return

def remove_duplicates():
	for item in numbers:
		check_unique_number(item)
	print(f"Unique numbers are: {unique_numbers}")

remove_duplicates()

