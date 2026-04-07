from bs4 import BeautifulSoup
import requests
import sys

url = 'http://books.toscrape.com/'

resposta = requests.get(url)
print(resposta)

if resposta.status_code == 200 :
    print("Conexão bem-sucedida!")
else:
    print ('Não foi possível realizar a conexão')
    sys.exit()

soup = BeautifulSoup(resposta.text, 'html.parser')
print(soup.title)

livros_html = soup.find_all('article', class_='product_pod')
print(len(livros_html))