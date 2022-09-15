# qrcode處理技術

- [利用Python做出QR Code](https://www.learnwithshin.com/post/%E5%88%A9%E7%94%A8python%E5%81%9A%E5%87%BAqr-code)

## [資料來源:Generate QRCode With Python In 5 lines](https://towardsdatascience.com/generate-qrcode-with-python-in-5-lines-42eda283f325)
```PYTHON
pip install pillow
pip install qrcode
```

```PYTHON
import qrcode
# Link for website
input_data = "https://towardsdatascience.com/face-detection-in-10-lines-for-beginners-1787aa1d9127"
#Creating an instance of qrcode
qr = qrcode.QRCode(
        version=1,
        box_size=10,
        border=5)
qr.add_data(input_data)
qr.make(fit=True)
img = qr.make_image(fill='black', back_color='white')
img.save('qrcode001.png')
```


## [資料來源:產生 QRCode ( 個性化 QRCode )](https://steam.oxxostudio.tw/category/python/example/qrcode.html)

```PYTHON
import os
os.chdir('/content/drive/MyDrive/Colab Notebooks')  # Colab 換路徑使用

import qrcode
img = qrcode.make('https://steam.oxxostudio.tw')    # 要轉換成 QRCode 的文字
img.show()                # 顯示圖片 ( Colab 不適用 )
img.save('qrcode.png')    # 儲存圖片
```


```PYTHON
import os
os.chdir('/content/drive/MyDrive/Colab Notebooks')  # Colab 換路徑使用

import qrcode
from qrcode.image.styledpil import StyledPilImage
from qrcode.image.styles.moduledrawers import VerticalBarsDrawer,RoundedModuleDrawer,HorizontalBarsDrawer,SquareModuleDrawer,GappedSquareModuleDrawer,CircleModuleDrawer

qr = qrcode.QRCode(
    version=1,
    error_correction=qrcode.constants.ERROR_CORRECT_L,
    box_size=10,
    border=4
)
qr.add_data('https://steam.oxxostudio.tw')
qr.make(fit=True)

img1 = qr.make_image(image_factory=StyledPilImage, module_drawer=SquareModuleDrawer())
img2 = qr.make_image(image_factory=StyledPilImage, module_drawer=GappedSquareModuleDrawer())
img3 = qr.make_image(image_factory=StyledPilImage, module_drawer=CircleModuleDrawer())
img4 = qr.make_image(image_factory=StyledPilImage, module_drawer=RoundedModuleDrawer())
img5 = qr.make_image(image_factory=StyledPilImage, module_drawer=VerticalBarsDrawer())
img6 = qr.make_image(image_factory=StyledPilImage, module_drawer=HorizontalBarsDrawer())
img1.save('qrcode1.png')
img2.save('qrcode2.png')
img3.save('qrcode3.png')
img4.save('qrcode4.png')
img5.save('qrcode5.png')
img6.save('qrcode6.png')
```

- QRCode 加入 logo 或圖片 
```PYTHON
import qrcode
from qrcode.image.styledpil import StyledPilImage

qr = qrcode.QRCode(
    version=1,
    error_correction=qrcode.constants.ERROR_CORRECT_L,
    box_size=10,
    border=4
)
qr.add_data('https://steam.oxxostudio.tw')
qr.make(fit=True)

img = qr.make_image(image_factory=StyledPilImage, embeded_image_path='mona.jpg')
img.save('qrcode.png')
```
