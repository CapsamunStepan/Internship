n = int(input('Enter a number: '))
a = list(filter(lambda x: n % x == 0, range(1, n + 1)))
print(a)
