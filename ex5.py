from random import randint


def fill():
    any_list = []
    size = randint(10, 20)
    for i in range(size):
        any_list.append(randint(10, 50))
    return any_list


a = fill()
b = fill()
# print(a)
# print(b)
common_elements = [x for x in a if x in b]
# print(common_elements)
