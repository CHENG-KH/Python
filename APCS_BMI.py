# BMI計算
# 
# 請輸入使用者身高(公尺)及體重(公斤)
# 計算其BMI數值，BMI=體重(公斤)/身高(公尺)^2
# 並判斷其健康狀態

# 重度肥胖：BMI >= 35
# 中度肥胖：30 <= BMI < 35
# 輕度肥胖：27 <= BMI < 30
# 過重：24 <= BMI < 27
# 正常範圍： 18.5 <= BMI <24
# 過輕：BMI < 18.5
# e.q. 輸入身高(1.75)體重(65)
# 顯示 BMI = 21.2, 健康狀態：正常範圍

height = float(input("請輸入身高(公尺)："))
weight = float(input("請輸入體重(公斤)"))

BMI = weight / ( height**2 )
print("BMI = ",BMI)

if BMI >= 35: 
    print("健康狀態：重度肥胖")
elif 30 <= BMI < 35:
    print("健康狀態：中度肥胖")
elif 27 <= BMI < 30:
    print("健康狀態：輕度肥胖")
elif 24 <= BMI < 27:
    print("健康狀態：過重")
elif 18.5 <= BMI <24:
    print("健康狀態：正常")
elif BMI < 18.5:
    print("健康狀態：過輕")
