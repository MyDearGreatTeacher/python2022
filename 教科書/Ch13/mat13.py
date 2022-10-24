import matplotlib.pyplot as plt
# 此變數用來儲存資料
scores = [10, 15, 80, 22, 93, 55, 88, 62, 45, 75, 81, 34, 99, 84, 85, 55, 58, 63, 68, 82, 84, 77, 69, 90, 100, 75, 65, 54, 34, 38, 48, 88, 71, 72, 5]
# 此變數用來儲存組距
bins = [0, 10, 20, 30, 40, 50, 60, 70, 80, 90, 100]
plt.hist(scores, bins, histtype = "bar")							# 繪製直方圖
plt.xlabel("Scores")												# 設定X軸的標籤
plt.ylabel("Students")											# 設定Y軸的標籤
plt.show()
