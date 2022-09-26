def CtoF1(degreeC):
    degreeF = degreeC * 1.8 + 32
    print("攝氏", degreeC, "度可以轉換成華氏", degreeF, "度")

temperatureC = eval(input("請輸入攝氏溫度："))
# 呼叫函式並傳遞攝氏溫度作為參數
CtoF1(temperatureC)
