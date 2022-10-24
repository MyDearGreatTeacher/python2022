import os
dir = "E:\\photo"
if os.path.exists(dir):
    os.rmdir(dir)
else:
    print("此資料夾不存在")
