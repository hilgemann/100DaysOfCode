html_doc = """
<html><head><title>The Dormouse's story</title></head>
<body>
<p class="title"><b>The Dormouse's story</b></p>

<p class="story">Once upon a time there were three little sisters; and their names were
<a href="http://example.com/elsie" class="sister" id="link1">Elsie</a>,
<a href="http://example.com/lacie" class="sister" id="link2">Lacie</a> and
<a href="http://example.com/tillie" class="sister" id="link3">Tillie</a>;
and they lived at the bottom of a well.</p>

<p class="story">...</p>
"""

from bs4 import BeautifulSoup
soup = BeautifulSoup(html_doc, 'html.parser')

print(soup.prettify())

print("print soup.title")
print(soup.title)
print("")
print("print soup.title.name")
print(soup.title.name)
print("")
print("print soup.title.string")
print(soup.title.string)
print("")
print("print soup.title.parent.name")
print(soup.title.parent.name)
print("")
print("print soup.p")
print(soup.p)
print("")
print("print soup.p['class']")
print(soup.p['class'])
print("")
print("print soup.a")
print(soup.a)
print("")
print("print soup.find_all('a')")
print(soup.find_all('a'))
print("")
print("print soup.find(id='link')")
print(soup.find(id="link3"))
print("")