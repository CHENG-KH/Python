
#跟大雄猜拳,大雄任意出拳(random)
#請使用者請使用者輸入一數字，分別代表以下猜拳的手勢 
#石頭 -> 0, 剪刀 -> 1, 布 -> 2
#顯示猜拳結果（輸，贏，平手 ）
#大0 -> 你0:平手
#大0 -> 你1:輸
#大0 -> 你2:贏
#大1 -> 你0:贏
#大1 -> 你1:平手
#大1 -> 你2:輸
#大2 -> 你0:輸
#大2 -> 你1:贏
#大2 -> 你2:平手
#五戰三勝(平手不算)
import random

nobita_win = list()
usr_win = list()
while len(nobita_win) != 3 and len(usr_win) != 3:
    print(nobita_win or usr_win)
    usr_input = int(input("請使用者請使用者輸入一數字，分別代表以下猜拳的手勢:石頭 -> 0, 剪刀 -> 1, 布 -> 2"))
    nobita_input = random.randint(0,2)
    print("大雄出的是：",nobita_input)
    if nobita_input == 0:
        if usr_input == 0:
            print("平手")
        if usr_input == 1:
            nobita_win.append("a")
            print("大雄贏")
        if usr_input == 2:
            usr_win.append("a")
            print("玩家贏")
    if nobita_input == 1:
        if usr_input == 0:
            usr_win.append("b")
            print("玩家贏")
        if usr_input == 1:
            print("平手")
        if usr_input == 2:
            nobita_win.append("b")
            print("大雄贏")
    if nobita_input == 2:
        if usr_input == 0:
            nobita_win.append("c")
            print("大雄贏")
        if usr_input == 1:
            usr_win.append("c")
            print("玩家贏")
        if usr_input == 2:
            print("平手")
print("遊戲結束")
