score = eval(input("請輸入數學分數 (0 ~ 100)："))
if score >= 90:   
    print("優等")
else:
    if score >= 80:
        print("甲等")
    else:
        if score >= 70:
            print("乙等")
        else:
            if score >= 60:
                print("丙等")
            else:
                print("不及格")

