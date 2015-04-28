# com isso consigo gerar atraves de um arquivo json, um dicionario onde posso agora tratar, e guardar informacoes 
#que desejar no Banco de Dados
import json
from pprint import pprint
with open('city.json') as data_file:
	d= json.load(data_file)

	pprint (d)