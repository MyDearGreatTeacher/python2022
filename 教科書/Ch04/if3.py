score = eval(input("請輸入數學分數 (0 ~ 100)："))
if score >= 90:   
    print("優等")
elif score < 90 and score >= 80:
    print("甲等")
elif score < 80 and score >= 70:
    print("乙等")
elif score < 70 and score >= 60:
    print("丙等")
else:
    print("不及格")

