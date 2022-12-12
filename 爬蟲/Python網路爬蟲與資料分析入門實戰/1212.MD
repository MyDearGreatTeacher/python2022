## cH1
- connect.py
```PYTHON
import requests
from bs4 import BeautifulSoup

resp = requests.get('https://jwlin.github.io/py-scraping-analysis-book/ch1/connect.html')
#resp.text
#resp.status_code
#resp.headers['content-type']
#resp.headers['Connection']
resp.headers['Date']
#https://developer.mozilla.org/en-US/docs/Glossary/Response_header
#soup = BeautifulSoup(resp.text, 'html.parser')
#print(soup.find('h1').text)
```
輸出結果:
```
<!DOCTYPE html>\n<html lang="en">\n  <head>\n    <meta charset="utf-8">\n    <meta http-equiv="X-UA-Compatible" content="IE=edge">\n    <meta name="viewport" content="width=device-width, initial-scale=1">\n    <!-- The above 3 meta tags *must* come first in the head; any other head content must come *after* these tags -->\n    <meta name="description" content="">\n    <meta name="author" content="">\n    \n    <title>Pycone 松果城市</title>\n\n    <!-- Bootstrap core CSS -->\n    <link href="bootstrap.min.css" rel="stylesheet">\n\n    <!-- IE10 viewport hack for Surface/desktop Windows 8 bug -->\n    <link href="https://getbootstrap.com/assets/css/ie10-viewport-bug-workaround.css" rel="stylesheet">\n\n    <!-- Custom styles for this template -->\n    <link href="https://getbootstrap.com/examples/sticky-footer/sticky-footer.css" rel="stylesheet">\n\n    <!-- Just for debugging purposes. Don\'t actually copy these 2 lines! -->\n    <!--[if lt IE 9]><script src="../../assets/js/ie8-responsive
```

```
<!DOCTYPE html>\n

<html lang="en">\n  

<head>\n    
  <meta charset="utf-8">\n    
  <meta http-equiv="X-UA-Compatible" content="IE=edge">\n    
  <meta name="viewport" content="width=device-width, initial-scale=1">\n   
<!-- The above 3 meta tags *must* come first in the head; any other head content must come *after* these tags -->\n    <meta name="description" content="">\n    
<meta name="author" content="">\n    \n    
<title>Pycone 松果城市</title>\n\n    
<!-- Bootstrap core CSS -->\n    
<link href="bootstrap.min.css" rel="stylesheet">\n\n    <!-- IE10 viewport hack for Surface/desktop Windows 8 bug -->\n    <link href="https://getbootstrap.com/assets/css/ie10-viewport-bug-workaround.css" rel="stylesheet">\n\n    <!-- Custom styles for this template -->\n    
<link href="https://getbootstrap.com/examples/sticky-footer/sticky-footer.css" rel="stylesheet">\n\n    

<!-- Just for debugging purposes. Don\'t actually copy these 2 lines! -->\n    <!--[if lt IE 9]><script src="../../assets/js/ie8-responsive

```


- try_connect.py 
```PYTHON
import requests
from bs4 import BeautifulSoup


def main():
    url1 = 'http://jwlin.github.io/py-scraping-analysis-book/ch1/connect.html'
    bad_url = 'http://non-existed.domain/connect.html'
    text1 = get_tag_text(url1, 'h1')
    print(text1)
    text2 = get_tag_text(url1, 'h2')
    print(text2)
    text3 = get_tag_text(bad_url, 'h1')
    print(text3)


def get_tag_text(url, tag):
    try:
        resp = requests.get(url)
        if resp.status_code == 200:
            soup = BeautifulSoup(resp.text, 'html.parser')
            return soup.find(tag).text
    except Exception as e:
        print('Exception: %s' %(e))
    return None


if __name__ == '__main__':
    main()
```
### requests
- [Requests: HTTP for Humans](https://requests.readthedocs.io/en/latest/)

## ch2

```PYTHON
import requests
from bs4 import BeautifulSoup


def main():
    resp = requests.get('http://jwlin.github.io/py-scraping-analysis-book/ch2/blog/blog.html')
    soup = BeautifulSoup(resp.text, 'html.parser')

    # 取得第一篇 blog (h4)
    print(soup.find('h4'))
    print(soup.h4)  # 與上一行相等

    # 取得第一篇 blog 主標題
    print(soup.h4.a.text)

    # 取得所有 blog 主標題, 使用 tag
    main_titles = soup.find_all('h4')
    for title in main_titles:
        print(title.a.text)

    # 取得所有 blog 主標題, 使用 class
    # 以下寫法皆相同:
    # soup.find_all('h4', 'card-title')
    # soup.find_all('h4', {'class': 'card-title'})
    # soup.find_all('h4', class_='card-title')
    main_titles = soup.find_all('h4', 'card-title')
    for title in main_titles:
        print(title.a.text)

    # 使用 key=value 取得元件
    print(soup.find(id='mac-p'))

    # 當 key 含特殊字元時, 使用 dict 取得元件
    # print(soup.find(data-foo='mac-foo'))  # 會導致 SyntaxError
    print(soup.find('', {'data-foo': 'mac-foo'}))

    # 取得各篇 blog 的所有文字
    divs = soup.find_all('div', 'content')
    for div in divs:
        # 方法一, 使用 text (會包含許多換行符號)
        #print(div.text)
        # 方法二, 使用 tag 定位
        #print(div.h6.text.strip(), div.h4.a.text.strip(), div.p.text.strip())
        # 方法三, 使用 .stripped_strings
        print([s for s in div.stripped_strings])


if __name__ == '__main__':
    main()
```



```PYTHON


```



```PYTHON


```



```PYTHON


```



```PYTHON


```



```PYTHON


```



```PYTHON


```



```PYTHON


```

```PYTHON


```


```PYTHON


```



```PYTHON


```



```PYTHON


```



```PYTHON


```



```PYTHON


```



```PYTHON


```



```PYTHON


```



```PYTHON


```

```PYTHON


```


```PYTHON


```



```PYTHON


```



```PYTHON


```



```PYTHON


```



```PYTHON


```



```PYTHON


```



```PYTHON


```



```PYTHON


```

```PYTHON


```


```PYTHON


```



```PYTHON


```



```PYTHON


```



```PYTHON


```



```PYTHON


```



```PYTHON


```



```PYTHON


```



```PYTHON


```

```PYTHON


```


```PYTHON


```



```PYTHON


```



```PYTHON


```



```PYTHON


```



```PYTHON


```



```PYTHON


```



```PYTHON


```



```PYTHON


```



