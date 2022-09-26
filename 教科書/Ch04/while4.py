answer = input("請輸入「快樂」的英文：")         # 將使用者輸入的資料存放在變數answer

while answer.upper() != "HAPPY":               # upper() 函式可以將字串轉換成大寫
    if answer.upper() == "QUIT":
        print("我不玩了！")
        break
    answer = input("答錯了，請重新輸入「快樂」的英文：")
else:
    print("答對了！")
