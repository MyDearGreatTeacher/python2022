while True:
    try:
        fileName = input("請輸入檔案名稱：")
        fileObject = open(fileName, "r")
        break
    except FileNotFoundError:
        print("找不到檔案！")

content = fileObject.read()	    # 讀取檔案
print(content)                  # 印出內容
fileObject.close()		        # 關閉檔案
