from bs4 import BeautifulSoup
import requests
import sys
import csv

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

dados_extraidos = []

for livro in livros_html:
    livro_titulo = livro.h3.a['title']
    livro_preco = livro.find('p', class_='price_color').text
    livro_atual = {
        "titulo": livro_titulo,
        "preco": livro_preco
    }
    dados_extraidos.append(livro_atual)

print(dados_extraidos)

with open('relatorios_livros.csv', mode='w', newline='', encoding='utf-8') as arquivo:
    escritor = csv.DictWriter(arquivo, fieldnames=['titulo', 'preco'])
    escritor.writeheader()
    escritor.writerows(dados_extraidos)

print('Relatório CSV gerado com sucesso!')