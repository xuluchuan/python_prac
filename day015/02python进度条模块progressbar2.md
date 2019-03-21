# python进度条模块progressbar2

## github地址

- https://github.com/WoLpH/python-progressbar

## 安装

- `pip install progressbar2`

## 使用

```python
import time
import progressbar

number_of_entry = 77
with progressbar.ProgressBar(max_value=number_of_entry) as bar:
    for i in range(number_of_entry):
        time.sleep(0.1)
        bar.update(i)

```

## 效果

```
100% (77 of 77) |########################| Elapsed Time: 0:00:07 Time:  0:00:07
```
