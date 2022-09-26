str1 = "Hello, World!"
# 使用for迴圈逐一印出字串的每個字元和 '-' 字元
for i in str1:
    # 將選擇性參數end設定為 ''，表示每次印出 '-' 字元就加上空字串
    print(i, '-', end = '')
