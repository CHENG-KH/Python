#假設一個玩家有3個骰子(1~6)
#模擬骰出值到3個6的過程，統計出骰的次數
import random
x = random.randint(1,6)
y = random.randint(1,6)
z = random.randint(1,6)
count = 0
while x != 6 or y !=6 or z != 6:
    x = random.randint(1,6)
    y = random.randint(1,6)
    z = random.randint(1,6)
    count = count + 1
    print(x,y,z)
print(count)
