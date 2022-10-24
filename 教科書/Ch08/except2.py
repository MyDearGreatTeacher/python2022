try:
    X = eval(input("請輸入被除數X："))
    Y = eval(input("請輸入除數Y："))
    Z = X / Y
except ZeroDivisionError:
    print("除數不得為0")
except Exception as e1:
    print(e1.args)
else:
    print("沒有捕捉到例外！X除以Y的結果等於", Z)
finally:
    print("離開try…except區塊")
