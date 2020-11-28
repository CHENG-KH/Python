#求一個3*3矩陣，對角線元素之和：
#測試 8 10  12
#     5  4  10
#     1  9  8
# x = [int(num) for num in input("請輸入矩陣第一行").split()]
# y = [int(num) for num in input("請輸入矩陣第二行").split()]
# z = [int(num) for num in input("請輸入矩陣第三行").split()]

# print("{}+{}+{}+{}+{}={}".format(x[0],x[2],y[1],z[0],z[2]))

import random
n = int(input("請輸入為幾Ｎ(3-9)行矩陣："))
x = random.randint(0,9)
# arr = [[16,15,7],[4,8,12],[9,9,6]]
# print(arr[0][1])
arr_1 = list()
for j in range(n):
    arr_2 = list()
    for k in range(n):
        x = random.randint(0,9)
        arr_2.append(x)
    arr_1.append(arr_2)
print(arr_1)
        
# total = 0
# for l in range(n):
#     # print(arr[l][l])
#     # print(arr[l][-l-1])
#     total += arr[l][l]
#     total += arr[l][-l-1]
# print(total)
# # print(total)
# # for i in range(1,n):
# #     for j in range(1,n):
