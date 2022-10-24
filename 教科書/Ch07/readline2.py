import os.path

if os.path.isfile("poem.txt"):
    fileObject = open("poem.txt", "r")
    for line in fileObject:
        print(line)
    fileObject.close()
else:
    print("此檔案不存在")


