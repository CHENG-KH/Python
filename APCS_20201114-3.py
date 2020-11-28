# 打印出所有的「水仙花數」，所謂的「水仙花數」是指一個三位數，其各位數字立方和等於該數本身。(while迴圈+字串拆值至陣列)
# 例如:153是一個水仙花數，因為153 = 1的三次方+5的三次方+3的三次方
import math
# print(x,y,z)
num = ()
total = 100
x = ()
y = ()
z = ()
for i in range(900):
    num = total + i
    # print(num)
    num_str = str(num)
    x = int(num_str[0])
    y = int(num_str[1])
    z = int(num_str[2])
    if x ** 3 + y ** 3 + z ** 3 == num:
        print(num)
    pass
