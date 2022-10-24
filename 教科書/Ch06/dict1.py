# 這個函式用來將字串中的特殊字元取代成空白
def replaceSymbols(string):
    for char in string:
        if char in "~!@#$%^&()[]{},+-*|/?<>'.;:\"":
            string = string.replace(char, ' ')
    return string

# 這個函式用來計算字串中每個單字的出現次數
def counts(string):
    wordlist = string.split()		# 根據空白將字串中每個單字分隔成串列
    for word in wordlist:			# 使用迴圈計算串列中每個單字的出現次數
        if word in result:
            result[word] = result[word] + 1
        else:
            result[word] = 1

song = "I have a pen. I have an apple, Apple pen. I have a pen. I have pineapple. \
    pineapple pen, Apple pen, Pineapple pen, Pen pineapple, apple pen."
# 這個空字典用來儲存每個單字的出現次數
result = {}
# 將歌詞轉換成小寫，然後呼叫replaceSymbols() 函式將特殊字元取代成空白
tmp = replaceSymbols(song.lower())
# 呼叫counts() 函式計算每個單字的出現次數
counts(tmp)
print(result)