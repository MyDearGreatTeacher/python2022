import matplotlib.pyplot as plt
# 此變數用來存放長條圖的X座標，根據智商分組所設定
x = [70, 80, 90, 100, 110, 120, 130, 140, 150]
# 此變數用來存放長條圖的Y座標，根據人數百分比所設定
y = [2.2, 5.3, 11.5, 19.7, 22.9, 19.6, 11.2, 5.5, 2.1]
# 此變數用來存放長條圖的刻度標籤，根據智商分組所設定
tl = ["<75", "75~84", "85~94", "95~104", "105~114", "115~124", "125~134", "135~144", ">144"]
# 建立寬度為8英吋、高度為4英吋的新圖表
plt.figure(figsize = (8, 4))
# 繪製長條圖
plt.bar(x = x, height = y, width = 5, tick_label = tl, label = "Sample1")
plt.legend()										# 放置圖例
plt.xlabel("Smarts")								# 設定X軸的標籤
plt.ylabel("Probability (%)")					# 設定Y軸的標籤
plt.title("Bar of IQ")							# 設定標題
plt.show()
