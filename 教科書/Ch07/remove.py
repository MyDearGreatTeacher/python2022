import os
file = "E:\\poem.txt"
if os.path.exists(file):
    os.remove(file)
else:
    print("此檔案不存在")
