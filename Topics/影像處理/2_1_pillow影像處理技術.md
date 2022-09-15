# pillow影像處理技術
- PIL(Pillow) 是 Python 中著名的影像處理套件
- 在 Python2 的時代是 PIL
- Python3 fork 出一個可相容新版的 Pillow
- 可用來轉檔、調色、濾鏡、浮水印甚至創造圖片一堆的功能
- 可透過程式語言批次處理大量的檔案

# pillow套件
- [Reference](https://pillow.readthedocs.io/en/stable/reference/index.html#)
  - [Image子模組](https://pillow.readthedocs.io/en/stable/reference/Image.html)
  - [ImageDraw子模組](https://pillow.readthedocs.io/en/stable/reference/ImageDraw.html)

# 安裝 pip install Pillow

# 圖片讀寫 ==>使用Image模組
- Image.open() 讀取圖片檔
- save("FILE NAME","FORMAT") 寫入圖片檔
  - format 其實非必須，PIL會自動透過常見副檔名來判斷格式。
- 免費圖片: pixabay 
```python
from PIL import Image

im = Image.open("test.jpg")  //建立 im 物件 再利用許多方法去處理
im.save("test.png","png")
//im.save("test.tiff","tiff")
//im.save("test.pdf","pdf")
```
## Image物件的屬性
-
## [資料來源1: 將目錄下所有 jpg 檔轉換為特定格式](https://ithelp.ithome.com.tw/articles/10226578)
- 更多範例請參考資料來源1
- 修改突變尺寸 == > resize()
- JPG 壓縮
- 圖片旋轉 == > transpose()
- 製作縮圖 == > thumbnail()
- 加入濾鏡  == > fliter()
-   == > 
-   == > 
-   == > 
```python
from glob import glob
from os.path import splitext
from PIL import Image
import sys

if(len(sys.argv) != 2):
    exit("參數錯誤")

userFormat = sys.argv[1]

jpglist = glob("*.[jJ][pP][gG]")

for jpg in jpglist:
    try:
        im = Image.open(jpg)
        pic = splitext(jpg)[0] + "." + userFormat
        im.save(pic)
        print(pic)
    except expression as identifier:
        print(identifier)
```

## [資料來源2:[Day 21] 從零開始學Python - 基本圖形處理Pillow：花下是誰對影成雙](https://ithelp.ithome.com.tw/articles/10247292)
