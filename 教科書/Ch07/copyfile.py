import os.path
import sys

sourcefile = input("請輸入來源檔案名稱 (*.txt)：")
targetfile = input("請輸入目的檔案名稱 (*.txt)：")

if os.path.isfile(targetfile):
    print("目的檔案已經存在，取消複製檔案！")
    sys.exit()

fileObject1 = open(sourcefile, "r")
fileObject2 = open(targetfile, "w")

content = fileObject1.read()
fileObject2.write(content)

fileObject1.close()
fileObject2.close()

print("檔案複製完畢！")


