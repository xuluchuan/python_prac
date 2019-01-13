# 运行python

## 运行python

### 1.编写.py结尾的文件 hello_world.py

> hello_world.py

``` python
print('Hello World!')
```

### 2.python FILE.py cmd运行此文件

- python 文件路径 回车

```
D:\develop\my\python\day001\code>python hello_world.py
Hello World!
```

### 3.中文

>hello_world_ch.py

``` python
print('你好，中国！')
```

```
D:\develop\my\python\day001\code>python hello_world_ch.py
你好，中国！
```

### 4.python2与3区别

- python2 默认编码是ascii码，不支持中文
- python3 默认编码是utf8，支持中文
- python2 解决：最上面一行 `# -*- encoding:utf-8 -*-`

## 变量 

- 运算的中间结果暂存在内存中，以便后续代码调用
- 命名规则1：数字，字母，下划线，任意组合，不能以数字开头
- 命名规则2：不能是python中的关键字 小写单词
- 命名规则3：变量具有可描述性
- 推荐：下划线连接小写字母命名 number_of_students
- 不推荐：中文
- age1 = 12 内存中开辟空间存放12，使用变量age1指向内存中的空间
- 赋值从右边开始算，赋值给左边的变量

```python
age1 = 12
age2 = age1
age3 = age2
age2 = 100
```

```
D:\develop\my\python\day001\code>python variables_age.py
12 100 12
```

## 常量

- 一直不变的量
- 推荐命名：全部大写，下划线连接 BIRTH_OF_AMERICA    

## 注释

- 方便自己和他人阅读理解代码

### 单行注释

- \#开头的行 或一行结尾后的#后面的内容

### 多行注释

- 上下各一对 三个单引号或三个双引号
