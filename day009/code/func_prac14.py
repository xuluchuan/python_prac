# 写函数，用户传入修改的文件名，与要修改的内容，执行函数，完成整个文件的批量修改操作

import os


def file_modify_content(file, old, new):
    """
    用户传入修改的文件名，与要修改的内容，执行函数，完成整个文件的批量修改操作
    :param file: 修改的文件名
    :param old: 修改前的内容
    :param new: 修改后的内容
    :return: None
    """
    with open(file, encoding='utf-8') as f1, open(file + '.bak', mode='w', encoding='utf-8') as f2:
        for line in f1:
            line = line.replace(old, new)
            f2.write(line)
    os.remove(file)
    os.rename(file + '.bak', file)


file_modify_content('a.txt', 'hello', 'Hello')
