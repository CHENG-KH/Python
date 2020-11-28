# name = input("Please enter your name:")
# print("Hello!",name)

# 取得使用者輸入的4個分數，顯示其加總及平均值

# score_1 = input("請輸入第一個分數：")
# score_2 = input("請輸入第二個分數：")
# score_3 = input("請輸入第三個分數：")
# score_4 = input("請輸入第四個分數：")

# #型別轉換，str -> int ，因為從input取出的數值，是str
# num_core_1 = int(score_1)
# num_core_2 = int(score_2)
# num_core_3 = int(score_3)
# num_core_4 = int(score_4)
# total = num_core_1+num_core_2+num_core_3+num_core_4
# print(total)

# score_1 = int(input("請輸入第一個分數："))
# score_2 = int(input("請輸入第二個分數："))
# score_3 = int(input("請輸入第三個分數："))
# score_4 = int(input("請輸入第四個分數："))
# #型別轉換，str -> int ，因為從input取出的數值，是str

# total = score_1+score_2+score_3+score_4
# average = total/4
# print(total, average)

# #如果全班平均成績大於60，顯示 請大家喝飲料
# #等於60，請喝養樂多
# #沒有的話，顯示 再加油
# if average > 60:
#     print("請大家喝飲料")
# elif average == 60:
#     print("請喝養樂多") 
# else:
#     print("再加油")

# average = total/4
# print(total, average)

# #如果全班平均成績大於60，顯示 請大家喝飲料
# #等於60，請喝養樂多
# #沒有的話，顯示 再加油
# if average > 60:
#     print("請大家喝飲料")
# elif average == 60:
#     print("請喝養樂多") 
# else:
#     print("再加油")

# scores = input()
# scores_array = scores.split()
# total = 0
# score_len = len(scores_array)
# for i in scores_array:
#     total += int(i) #將str變成int,然後相加
# average = total / score_len
# print("總分:{}, 平均:{:.2f}".format(total,average))
# # #{}可以用.format(total,average)來取代前面數字
# # #.2f->小數點後2位

scores = input()
scores_array = scores.split()
scores_num_array = list(map(int,scores_array)) # map 可以執行（function,array)
total = 0
score_len = len(scores_num_array)
for i in scores_num_array:
    total += i
# total = total + i
average = total / score_len
print("總分:{}, 平均:{:.2f}".format(total,average))
