def outer():
    a = 1

    def inner():
        nonlocal a
        a += 1
        print(a)

    inner()


outer()
