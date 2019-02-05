# 编写下载网页内容的函数，要求功能是：用户传入一个url，函数返回下载页面的结果
from urllib.request import urlopen
import os


def cache(func):
    def inner(*args, **kwargs):
        for url in args:
            url = url.replace(':', '#').replace('/', '@')
            path = url + '.cache'
            if os.path.exists(path) and os.path.getsize(path) > 0:
                with open(path, mode='rb') as f:
                    ret = f.read()
                    return ret
            else:
                with open(path, mode='wb') as f:
                    ret = func(*args, **kwargs)
                    f.write(ret)
                    return ret

    return inner


@cache
def download_page(url):
    ret = urlopen(url).read()
    return ret


result = download_page('https://www.cnblogs.com/shaosks/p/5614630.html')
print(result)
result = download_page('https://www.baidu.com')
print(result)
