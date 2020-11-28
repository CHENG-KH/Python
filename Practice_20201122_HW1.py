# 輸入為一行含有一個十進位表示法的正整數X，之後是一個換行字元。
x = [int(num) for num in input("輸入為一行含有一個十進位表示法的正整數X:")]
# print(len(x))
# print(type(len(x)))
odd = list()
even = list()
count = 0
i = int()
# odd.append(x[0])
for i in range(len(x)):
    if count % 2 == 0:
        even.append(x[i])
        count += 1
    else:
        odd.append(x[i])
        count += 1
print(odd)
print(even)
sum_odd = 0
sum_even = 0
for j in odd:
    sum_odd += j
print(sum_odd)
for k in even:
    sum_even += k
print(sum_even)
print(abs(sum_odd - sum_even))
