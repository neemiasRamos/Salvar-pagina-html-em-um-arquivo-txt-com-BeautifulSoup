import requests
from bs4 import BeautifulSoup
 
url = "URL DO SITE"
url_get = requests.get(url)
soup = BeautifulSoup(url_get.content, 'lxml')
 
with open('G:\\NOVA PASTA\\html-copiado.txt', 'w', encoding='utf-8') as f_out:
    f_out.write(soup.prettify())
