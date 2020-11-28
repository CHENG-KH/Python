#第一行有整數n(0<n<100)代表有幾個數
#第二行有n個數A1...An(0<An<100)表示每個磁鐵上的數字
#第一行請輸出最一開始的狀態
#第二行開始，輸出「刪去第一項後，全部倒轉的結果」，直到數字只剩下一個為止

a = int(input("請輸入1-99其中一個整數"))
m = input("請輸入每個磁鐵的數字")
m_split = m.split()
m_int = list(map(int,m_split))

for i in m_int: 
    print(i,end=' ')
print()

while a != 1:
    a = a - 1
    del m_int[0]
    m_int.reverse()
    for j in m_int:
        print(j,end=' ')
    print()
