# 平台建置
- 先安裝PYTHON
- 更新PIP
```
python.exe -m pip install --upgrade pip
```
- 安裝FLASK
```
pip install flask
```


## 使用 notepad++開發第一支程式 app1.py
```python
from flask import Flask
app = Flask(__name__)

@app.route('/')
def index():
    return '歡迎來到首頁!'

@app.route('/hello')
def hello():
    return '歡迎來到歡迎頁面!'

if __name__ == '__main__':
    app.run()
```
## 執行程式 python app1.py
## 成功畫面 ![]()

