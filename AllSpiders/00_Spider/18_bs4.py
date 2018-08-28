# coding=utf-8

from bs4 import BeautifulSoup
import re

html = """
<html><head><title>The Dormouse's story</title></head>
<body>
<p class="title" name="dromouse"><b>The Dormouse's story</b></p>
<p class="story">Once upon a time there were three little sisters; and their names were
<a href="http://example.com/elsie" class="sister" id="link1"><!-- Elsie --></a>,
<a href="http://example.com/lacie" class="sister" id="link2">Lacie</a> and
<a href="http://example.com/tillie" class="sister" id="link3">Tillie</a>;
and they lived at the bottom of a well.</p>
<p class="story">...</p>
"""

#创建 Beautiful Soup 对象
soup = BeautifulSoup(html,'lxml')

#打开本地 HTML 文件的方式来创建对象
#soup = BeautifulSoup(open('index.html'))

#格式化输出 soup 对象的内容
# print soup.prettify()

# print soup.title
# print soup.head
# print soup.a
# print soup.p
# print type(soup.p)
# print soup.name

# print soup.head.name
# print soup.p.attrs
# print soup.p['class']
# soup.p['class'] = "newClass"
# print soup.p.get('class')
# print soup.p
# del soup.p['class']
# print soup.p

# print soup.p.string
# print type(soup.p.string)

# print type(soup.name)
# print soup.name
# print soup.attrs

# print soup.a
# print soup.a.string
# print type(soup.a.string)

# print soup.head.contents
# print soup.head.contents[0]

# print soup.head.children # 可以发现它是一个 list 生成器对象
# for child in soup.body.children:
#     print child

# for child in soup.descendants:
#     print child

# print soup.head.string
# print soup.title.string

# print soup.find_all('b')
# print soup.find_all('a')

# for tag in soup.find_all(re.compile("^b")):
#     print tag.name

# print soup.find_all(["a", "b"])

# print soup.find_all(id='link2')

# print soup.find_all(text='Elsie')
# print soup.find_all(text=["Tillie", "Elsie", "Lacie"])
# print soup.find_all(text=re.compile("Dormouse"))

# print soup.select('title')
# print soup.select('a')
# print soup.select('b')
# print soup.select('.sister')
# print soup.select('#link1')
# print soup.select('p #link1')
# print soup.select("head > title")
# print soup.select('a[class="sister"]')
# print soup.select('a[href="http://example.com/elsie"]')
# print soup.select('p a[href="http://example.com/elsie"]')

print type(soup.select('title'))
print soup.select('title')[0].get_text()

for title in soup.select('title'):
    print title.get_text()
