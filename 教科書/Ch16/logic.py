# 匯入套件與函式
import pandas as pd
from sklearn import datasets
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