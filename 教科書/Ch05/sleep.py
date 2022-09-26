import time

secs = eval(input("請輸入要倒數的秒數：")) 

for i in range(secs, 0, -1):
    print("倒數", i, "秒...")
    time.sleep(1)

print("時間到！")
        


