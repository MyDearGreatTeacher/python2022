# Python_Redis實務演練
## 參考資料
- [Redis 教程](https://www.runoob.com/redis/redis-tutorial.html)
- [Python redis 使用介绍](https://www.runoob.com/w3cnote/python-redis-intro.html)
## 安裝 redis 模組
```
Python 要使用 redis，需要先安裝 redis 模組：

sudo pip3 install redis
或
sudo easy_install redis
或
sudo python setup.py install
```
## 
```python
import redis   # 導入redis 模組

r = redis.Redis(host='localhost', port=6379, decode_responses=True)  
r.set('name', 'runoob')  # 設置 name 對應的值
print(r['name'])
print(r.get('name'))  # 取出鍵 name 對應的值
print(type(r.get('name')))  # 查看類型
```
```python
import redis    

pool = redis.ConnectionPool(host='localhost', port=6379, decode_responses=True)
r = redis.Redis(host='localhost', port=6379, decode_responses=True)  
r.set('name', 'runoob')  # 設置 name 對應的值
print(r.get('name'))  # 取出鍵 name 對應的值
```
