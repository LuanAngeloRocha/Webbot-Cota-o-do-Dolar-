from bs4 import BeautifulSoup
import requests
import json

link = "https://www.dolarhoje.net.br/dolar-comercial/"
site = requests.get(link)

html = site.content

soup = BeautifulSoup(html, 'html.parser')

conteudos = soup.find_all('p') #Pega todos os paragrafos do site

a = []
for conteudo in conteudos:
#        print('-=-'*12)
 #       print(conteudo)
  #      print("-=-"*12)
	a.append(conteudo.contents[0])
dados = []
for conteudo in a:
	try:
		cont = int(conteudo[0])
		dados.append(conteudo)
	except:
		pass
valor = []
data = []

#Separa as datas 
for dado in dados:
	data.append(dado[:10]) #[:10] pega os dez primeiros caracteres da string 
for dado in dados:
	v = float (dado[15:].replace(',','.'))
	valor.append(v)
print ('---'*8)
print ('COTAÇÂO DO DOLAR EM 2021')
print ('---'*8)
for x in range (len(valor)):
	print ('VALOR: R$',valor [x])
	print ('DATA:', data[x])
	print ('---'*7)

dados_dict =[]
for x in range (len(valor)):
	dados_dict.append({
		'data': data[x],
		'valor': valor[x]
	})
with open('dados.json', 'w') as f:
        json.dump(dados_dict, f, indent = 4, sort_keys=True)
        print("Dados salvos com sucesso!")


