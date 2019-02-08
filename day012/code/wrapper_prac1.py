wrapper_flag = True


def wrapper_outer(flag):
    def wrapper(func):
        def inner(*args, **kwargs):
            if flag:
                print('wrapper')
                ret = func(*args, **kwargs)
                return ret
            else:
                ret = func(*args, **kwargs)
                return ret

        return inner

    return wrapper


@wrapper_outer(wrapper_flag)
def f():
    print('f')


f()
