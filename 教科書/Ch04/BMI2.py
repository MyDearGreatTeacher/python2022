height = eval(input("請輸入身高 (公分)："))
weight = eval(input("請輸入體重 (公斤)："))
BMI = weight / (height / 100) ** 2
print("身高{0}公分、體重{1}公斤的BMI為{2}".format(height, weight, BMI))

if BMI < 18.5:
    print("過輕")
elif BMI >= 18.5 and BMI <= 24:
    print("正常")
elif BMI > 24 and BMI <= 27:
    print("過重")
elif BMI > 27 and BMI <= 35:
    print("肥胖")
elif BMI > 35:
    print("極肥胖")
