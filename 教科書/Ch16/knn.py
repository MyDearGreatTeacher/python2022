# 匯入套件與函式
from sklearn import datasets
from sklearn.model_selection import train_test_split
from sklearn.neighbors import KNeighborsClassifier
from sklearn import metrics
import matplotlib.pyplot as plt

# 匯入資料
iris = datasets.load_iris()
X = iris.data
y = iris.target
print(X)
print(y)

# 準備機器學習的訓練集與測試集
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size = 0.3, random_state = 0)
print("訓練集的維度:", X_train.shape)
print("測試集的維度:", X_test.shape)

# 建立與訓練KNN模型
model = KNeighborsClassifier(n_neighbors = 3)
model.fit(X_train, y_train)

# 分類預測結果
y_pred = model.predict(X_test)
print('目標值:', y_test)
print('預測值:', y_pred)
print('準確率:', model.score(X_test, y_test))

# 找出適當的K值
accuracy = []
for K in range(3, 100):
    model = KNeighborsClassifier(n_neighbors = K)
    model.fit(X_train, y_train)
    y_pred = model.predict(X_test)
    accuracy.append(metrics.accuracy_score(y_test, y_pred))
K = range(3, 100)
plt.plot(K, accuracy)
plt.show()