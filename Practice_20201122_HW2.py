line1_ary = list(map(int,input("請輸入3個整數：").split
line2_ary = list(map(int,input("請輸入3個整數：").split
n = int(input("請輸入一個正整數"))

a1 = line1_ary[0]
b1 = line1_ary[1]
c1 = line1_ary[2]
a2 = line2_ary[0]
b2 = line2_ary[1]
c2 = line2_ary[2]

ary = []

for i  in range(n+1):
    x1 = i
    x2 = -i+n
    # print(x1 , x2)
    
    y1 = a1 * (x1**2) + b1 * x1 + c1
    y2 = a2 * (x2**2) + b2 * x2 + c2
    
    ary.append(y1+y2)
    # print(y1+y2)

    pass

print(max(ary))
-----------------------------------------------------------

# 輸入為一行含有一個十進位表示法的正整數X，之後是一個換行字元。
#精簡版(count)
# num = input("請輸入正整數:")
# count = 0
# odd = 0
# even = 0
# for i in range(len(num)):
#     if count % 2 == 0:
#         even += eval(num[i])
#         count += 1
#     else:
#         odd += eval(num(i))
#         count += 1
# num_abs = abs(even - odd)
# print(num_abs)

#更精簡版(slices)
num = input("請輸入正整數:")
odd = [eval(i) for i in num[0::2]]
sum_odd = sum(odd)
even = [eval(i) for i in num[1::2]]
sum_even = sum(even)
num_abs = abs(sum_even - sum_odd)
print(num_abs)
