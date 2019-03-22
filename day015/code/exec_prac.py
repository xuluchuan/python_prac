i = 2
j = 3
exec("ans = i + j")
print("Answer is: ", ans)
print(eval("i + j"))
str1 = "for i in range(0,10): print(i)"
c = compile(str1, '', 'exec')
exec(c)
exec(c)
