fruits = {"蘋果": "apple", "鳳梨": "pineapple", "水蜜桃": "peach",           
    "香蕉": "banana", "西瓜": "watermelon", "葡萄": "grape",  
    "橘子": "orange", "番茄": "tomato", "奇異果": "kiwifruit"}

    
print("水果字典中的水果名稱：", tuple(fruits.keys()))
Q = input("請輸入要查詢英文的水果名稱：")
print(fruits.get(Q,"水果字典中沒有這種水果"))
