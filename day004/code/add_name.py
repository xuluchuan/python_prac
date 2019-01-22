list_emp_name = ['小红', '小明']
while True:
    new_emp = input('请输入新员工的姓名,q或Q键退出：')
    if new_emp:
        if new_emp.upper().strip() == 'Q':
            print('当前员工列表为', list_emp_name)
            break
        else:
            list_emp_name.append(new_emp.strip())
            print('当前员工列表为', list_emp_name)
    else:
        print('姓名不能为空')
