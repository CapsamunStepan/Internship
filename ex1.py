name = input('Enter your name: ')
age = int(input("Enter your age: "))
current_year = 2022
year = current_year + 100 - age
# extras
n = int(input("Enter number of copies you want to print: "))
print(f'{name}, you will be 100 years old in {year} \n' * n)
