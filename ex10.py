from random import randint


def fill():
    any_list = []
    size = randint(10, 30)
    for i in range(size):
        any_list.append(randint(10, 20))
    return any_list


a = [1, 1, 2, 3, 5, 8, 13, 21, 34, 55, 89]
b = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13]
result = list(set(a) & set(b))
print(result)

list1 = fill()
list2 = fill()
# print(list1)
# print(list2)
result = list(set(list1) & set(list2))
print(result)
