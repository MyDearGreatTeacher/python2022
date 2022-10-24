# 匯入套件與函式
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
from sklearn import datasets
from matplotlib.colors import ListedColormap
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import StandardScaler
from sklearn.linear_model import LogisticRegression

# 匯入資料
iris = datasets.load_iris()
X = pd.DataFrame(iris.data, columns = iris.feature_names)
y = pd.DataFrame(iris.target, columns = ['target'])
iris = pd.concat([X, y], axis = 1)
print(iris)

# 取出要進行邏輯迴歸的資料
iris = iris[['sepal length (cm)', 'petal length (cm)', 'target']]
iris = iris[iris['target'].isin([0, 1])]
print(iris)

# 準備機器學習的訓練集與測試集
X = iris[['sepal length (cm)', 'petal length (cm)']]
y = iris[['target']]
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size = 0.3, random_state = 0)
print("訓練集的維度:", X_train.shape)
print("測試集的維度:", X_test.shape)

# 將資料標準化 (平均值為0、標準差為1)
X_train_std = StandardScaler().fit_transform(X_train)
X_test_std = StandardScaler().fit_transform(X_test)

# 建立與訓練邏輯迴歸模型
model = LogisticRegression()
model.fit(X_train_std, y_train['target'])

# 分類預測結果
y_pred = model.predict(X_test_std)
print('目標值:', y_test['target'].values)
print('預測值:', y_pred)
print('準確率:', model.score(X_test_std, y_test))

X = X_test_std
y = y_test['target'].values
markers = ('o', '^')
colors = ('red', 'green')
cmap = ListedColormap(colors[:len(np.unique(y))])
x0min, x0max = X[:, 0].min() - 1, X[:, 0].max() + 1
x1min, x1max = X[:, 1].min() - 1, X[:, 1].max() + 1
a, b = np.meshgrid(np.arange(x0min, x0max, 0.01), np.arange(x1min, x1max, 0.01)) 
Z = model.predict(np.array([a.ravel(), b.ravel()]).T) 
Z = Z.reshape(a.shape)
plt.figure(figsize = (9, 6))
plt.contourf(a, b, Z, alpha = 0.3, cmap = cmap)
plt.xlim(a.min(), a.max())
plt.ylim(b.min(), b.max())
for i, t in enumerate(np.unique(y)):  
    p = X[y == t]
    plt.scatter(x = p[:, 0],  y = p[:, 1], c = cmap(i), marker = markers[i],  label = t)
plt.xlabel('sepal length [standardized]', size = 20)
plt.ylabel('petal length [standardized]', size = 20)
plt.legend(loc='upper left')
plt.show()