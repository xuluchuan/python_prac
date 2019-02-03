from urllib.request import urlopen


def get_url():
    url = 'http://www.baidu.com'

    def get():
        ret = urlopen(url).read()
        print(ret)

    return get


get_func = get_url()
get_func()
get_func()
