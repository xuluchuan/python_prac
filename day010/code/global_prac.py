a = 3


def change_a():
    a = 4


change_a()
print(a)


def change_a2():
    global a
    a = 4


change_a2()
print(a)


def print_a():
    print(a)


print_a()


def add_a():
    a += 1


add_a()
print(a)
