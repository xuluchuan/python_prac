def outer():
    a = 1
    print(locals())

    def inner():
        b = 1
        print(globals())
        print(locals())

    inner()


outer()
