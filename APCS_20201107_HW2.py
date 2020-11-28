a = [int(num) for num in input("請輸入你的三個幸運數字").split()]
b = [int(num) for num in input("請輸入你的五個號碼區號碼").split()]
c = [int(num) for num in input("請輸入你的五個號碼相對應的金額你的五個號碼相對應的金額").split()]
# correct_num = list()
bonus = ()
# for a in x:
if a[0] and a[1] and a[2] in b:
    # correct_num.append(a[0])
    # correct_num.append(a[1])
    # print(a[0],a[1])
    #print(c[b.index(a[0])] + c[b.index(a[1])])
    bonus = c[b.index(a[0])] + c[b.index(a[1])] - c[b.index(a[2])]
    if bonus < 0:
        print(0)
    if bonus >= 0:
        print("獎金為：{}".format(bonus))
elif a[0] and a[1] in b:
    bonus = (c[b.index(a[0])] + c[b.index(a[1])])*2
    print("獎金為：{}".format(bonus))
else:
    print("獎金為：0")
