# 使用 "a" 模式開啟檔案以將資料附加到原檔案內容的後面
fileObject = open("E:\\poem.txt", "a")

# 寫入檔案，\n 字元表示換行
fileObject.write("\n鳳凰臺上鳳凰遊，鳳去臺空江自流。")
fileObject.write("\n吳宮花草埋幽徑，晉代衣冠成古邱。")
fileObject.write("\n三山半落青又外，二水中分白鷺洲。")
fileObject.write("\n總為浮雲能蔽日，長安不見使人愁。")

# 關閉檔案
fileObject.close()
