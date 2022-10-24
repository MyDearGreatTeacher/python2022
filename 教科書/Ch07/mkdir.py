import os
dir = "E:\\photo"
if not os.path.exists(dir):
    os.mkdir(dir)
else:
    print("此資料夾已經存在")
