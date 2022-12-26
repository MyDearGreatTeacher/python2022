
# Selenium
- 安裝套件
```
pip3 install selenium
```
![image](https://user-images.githubusercontent.com/71476447/209459693-8c971d84-d8b9-4a0d-9c75-45268c3aecf8.png)

- 安裝ChromeDrive
- [chromedriver](https://chromedriver.chromium.org/downloads)
- 查看Chrome 版本
- 設定 -> 關於Chrome -> Chrome版本
- 下載後解壓縮到,程式碼的目錄底下

![image](https://user-images.githubusercontent.com/71476447/209459763-c83e5074-dac7-4982-893e-ad0d85e9ca3d.png)
![image](https://user-images.githubusercontent.com/71476447/209459758-45c932cc-3502-4cfb-903b-75bd9a118a44.png)

```
from selenium import webdriver
web = webdriver.Chrome('chromedrive.exe')
web.get('http://www.twse.com.tw/zh/')
```

![image](https://user-images.githubusercontent.com/71476447/209459784-a299d4f2-678b-4708-89cf-4193e5ebfd24.png)
