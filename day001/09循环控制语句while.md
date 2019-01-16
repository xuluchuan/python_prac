# 循环控制语句while

- 满足条件执行循环体语句，直到不满足条件为止

```python
初始化语句
while 条件:
    循环体
    流程控制语句
```

```python
while True:
    print('1')
    print('1')
print('2')
```

- flag位：flag = True 
- break 终止循环
- continue 中止本次循环，开启下次循环

>sum100.py

```python
count = 1
sum100 = 0
while count <= 100:
    sum100 += count
    count += 1
print(sum100)
```

```
PS D:\xuluchuan\class\python\python_prac\day001\code> python .\break_demo.py

*
**
***
****
*****
******
*******
********
*********
```

- 利用flag位跳出双重循环

>break_demo.py

```python
i = 0
flag = False
while i < 100:
    j = 0
    while j < i:
        print('*', end='')
        if j == 8:
            flag = True
            break
        j += 1
    if flag:
        break
    print()
    i += 1
```

```
PS D:\xuluchuan\class\python\python_prac\day001\code> python .\break_demo.py

*
**
***
****
*****
******
*******
********
*********
```

- continue要放在流程控制语句之后

> continue_demo.py

```python
i = 0
while i <= 100:
    i += 1
    if i % 2 == 0:
        continue
    print(i, end=' ')
```

```
PS D:\xuluchuan\class\python\python_prac\day001\code> python .\continue_demo.py
1 3 5 7 9 11 13 15 17 19 21 23 25 27 29 31 33 35 37 39 41 43 45 47 49 51 53 55 57 59 61 63 65 67 69 71 73 75 77 79 81 83 85 87 89 91 93 95 97 99 101
```
