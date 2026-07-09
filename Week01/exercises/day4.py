# multiplication table
table_for = int(input("Enter a number to print its multiplication table: "))
for i in range(1, 11):
    print(f"{table_for} x {i} = {table_for * i} \n")

# sum of all number upto user specified
input_number = int(input('Enter a number to find sum: '))
total = 0;
for i in range(1, input_number + 1):
    total += i;
print(f"Sum of all numbers from 1 to {input_number} is: {total}")
    
# with list of techologies
technologies = ['Python', 'Java', 'C++', 'JavaScript', 'Go', 'Ruby']
total_tech = len(technologies)
# use index and sum
for i, tech in enumerate(technologies):
    print(f"{i+1}: {tech}")
print(f"Total number of technologies: {total_tech}")
