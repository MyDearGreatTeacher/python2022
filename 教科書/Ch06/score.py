# 串列變數list1用來存放5位評審給某位選手的分數，初始值為空串列
list1 = []

# 使用for迴圈要求輸入分數，然後呼叫append() 方法將分數加入串列的尾端
for i in range(1, 6):
    prompt = "請輸入第" + str(i) + "位評審的分數："
    score = eval(input(prompt))
    list1.append(score)

# 呼叫sum() 方法計算總分，然後印出結果
print("這位選手的總分為", sum(list1))
