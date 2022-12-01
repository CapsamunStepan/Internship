n = int(input('Enter any number: '))

if n % 4 == 0:
    print(f'Number {n} is multiple of 4')
if n % 2:
    print(f'Number {n} is odd')
else:
    print(f'Number {n} is even')

num = int(input('Enter any number: '))
check = int(input('Enter another number: '))

if check % num == 0:
    print(f'{check} is divided into {num}')
else:
    print(f"{check} isn't divided into {num}")
