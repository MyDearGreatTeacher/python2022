# [scikit-image](https://scikit-image.org/docs/stable/api/skimage.html)
-
- 子模組套件Subpackages:
  - color(各種影像色彩轉換)   Color space conversion.
  - data    Test images and example data.
  - draw    Drawing primitives (lines, text, etc.) that operate on NumPy arrays.
  - exposure  Image intensity adjustment, e.g., histogram equalization, etc.
  - feature(各種影像特徵分析)  Feature detection and extraction, e.g., texture analysis corners, etc.
  - filters(各種影像過濾)   Sharpening, edge finding, rank filters, thresholding, etc.
  - graph  Graph-theoretic operations, e.g., shortest paths.
  - io  Reading, saving, and displaying images and video.
  - measure  Measurement of image properties, e.g., region properties and contours.
  - metrics  Metrics corresponding to images, e.g. distance metrics, similarity, etc.
  - morphology(各種影像變形)  Morphological operations, e.g., opening or skeletonization.
  - restoration  Restoration algorithms, e.g., deconvolution algorithms, denoising, etc.
  - segmentation(各種影像切割) Partitioning an image into multiple regions.
  - transform(各種影像幾何轉換)  Geometric and other transforms, e.g., rotation or the Radon transform.
  - util Generic utilities.

viewer
A simple graphical user interface for visualizing results and exploring parameters.

# 範例學習 1
```python
from skimage import data, io, filters

# 載入圖片... or any other NumPy array!
image = data.coins()
io.imshow(image)
io.show()

# 圖片過濾  使用skimage.filters.sobel()
edges = filters.sobel(image)
io.imshow(edges)
io.show()
```
# 範例學習2 :彩色圖片轉成灰階圖片
- skimage.color.rgb2gray
- [RGB to grayscale](https://scikit-image.org/docs/stable/auto_examples/color_exposure/plot_rgb_to_gray.html#sphx-glr-auto-examples-color-exposure-plot-rgb-to-gray-py)
```python
import matplotlib.pyplot as plt

from skimage import data
from skimage.color import rgb2gray

original = data.astronaut()
grayscale = rgb2gray(original)

fig, axes = plt.subplots(1, 2, figsize=(8, 4))
ax = axes.ravel()

ax[0].imshow(original)
ax[0].set_title("Original")
ax[1].imshow(grayscale, cmap=plt.cm.gray)
ax[1].set_title("Grayscale")

fig.tight_layout()
plt.show()
```

# 範例學習

- []()
- []()
- []()
- []()
- []()
- []()
- [影像處理Handling Video Files](https://scikit-image.org/docs/stable/user_guide/video.html#moviepy)
