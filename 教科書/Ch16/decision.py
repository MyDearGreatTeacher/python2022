# 匯入套件與函式
from sklearn import datasets
from sklearn.model_selection import train_test_split
from sklearn.tree import DecisionTreeClassifier

# 匯入資料
iris = datasets.load_iris()
X = iris.data
y = iris.target

# 準備機器學習的訓練集與測試集
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size = 0.3, random_state = 0)

# 建立與訓練決策樹模型
model = DecisionTreeClassifier()
model.fit(X_train, y_train)

# 分類預測結果
y_pred = model.predict(X_test)
print('目標值:', y_test)
print('預測值:', y_pred)
print('準確率:', model.score(X_test, y_test))
