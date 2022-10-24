# 匯入套件與函式
import pandas as pd   
import matplotlib.pyplot as plt
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LinearRegression
from sklearn.metrics import mean_squared_error

# 匯入資料
df = pd.read_csv("data.csv")
X = df.drop('Weight', axis = 1)
y = df['Weight']

# 準備機器學習的訓練集與測試集
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size = 0.2, random_state = 0)
print("訓練集的維度:", X_train.shape)
print("測試集的維度:", X_test.shape)

# 建立與訓練線性迴歸模型
model = LinearRegression()
model.fit(X_train, y_train)
print("係數 (Coeficient):", model.coef_)
print("截距 (Interception):", model.intercept_)

# 使用模型進行預測並計算MSE (均方差)
y_pred = model.predict(X_test)
MSE = mean_squared_error(y_test, y_pred)
print("MSE:", MSE)

# 繪製身高與體重散佈圖以及線性迴歸分析圖
plt.scatter(X, y, color = "blue")
plt.plot(X_test, y_pred, color = "red")
plt.xlabel("Height")
plt.ylabel("Weight")
plt.show()