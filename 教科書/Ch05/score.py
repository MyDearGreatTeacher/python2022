def checkScore(score):
    if score < 0 or score > 100:
        print("分數超過範圍！")
        return
    if score >= 60:
        print("及格！")
    else:
        print("不及格！")

s = eval(input("請輸入數學分數 (0 ~ 100)："))
checkScore(s)
