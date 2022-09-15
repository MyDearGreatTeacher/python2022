# pillow影像處理技術
- PIL(Pillow) 是 Python 中著名的影像處理套件
- 在 Python2 的時代是 PIL
- Python3 fork 出一個可相容新版的 Pillow
- 可用來轉檔、調色、濾鏡、浮水印甚至創造圖片一堆的功能
- 可透過程式語言批次處理大量的檔案

# pillow套件
- [Reference](https://pillow.readthedocs.io/en/stable/reference/index.html#)


# 安裝 pip install Pillow

# 圖片讀寫 ==>使用Image模組
- Image.open() 讀取圖片檔
- save("FILE NAME","FORMAT") 寫入圖片檔
  - format 其實非必須，PIL會自動透過常見副檔名來判斷格式。
```python
from PIL import Image

im = Image.open("test.jpg")
im.save("test.png","png")
//im.save("test.tiff","tiff")
```
