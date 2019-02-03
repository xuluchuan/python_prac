def outer():
    a = 1

    def inner():
        print(inner.__closure__)

    inner()


outer()
