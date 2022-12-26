# yfinance模組技巧
- [yfinance GitHub原始碼](https://github.com/ranaroussi/yfinance)



## 實作
- [元大台灣50 (0050.TW)](https://hk.finance.yahoo.com/quote/0050.TW?p=0050.TW&.tsrc=fin-srch)
- GOOGLE COLAB
  - !pip install yfinance
  - 範例程式
```python
import yfinance as yf
a=yf.download('0050.tw',start='2022-12-20',end='2022-12-26')
a
```
- type(a)
