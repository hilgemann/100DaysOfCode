from bs4 import BeautifulSoup
import requests

# URL = "https://amzn.to/4bIEXKB"

URL = "https://www.amazon.com.br/Tênis-Nike-SB-Chron-Masculino/dp/B09BJ7C57T"

headers = { 'user-agent': "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/123.0.0.0 Safari/537.36 OPR/109.0.0.0 (Edition utorrent)"}

response = requests.get(URL, headers=headers)

soup = BeautifulSoup(response.content, 'lxml')

print(soup.prettify())

title_element = soup.select_one('#productTitle')

title = title_element.text.strip()

print(title)

# rating_element = soup.select_one('#acrPopover')

# rating = rating_element

# print(rating)
