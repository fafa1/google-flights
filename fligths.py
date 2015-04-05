
#criando tabela, conectando
import dataset
import time

db=dataset.connect('sqlite:///banco.db') #nome do banco de dados
table=db['city'] # nome da tabela


d=time.strftime('%d/%m/%y')

table.insert(dict(cidade_origem='salvador', cidade_destino='sao paulo',data_saida='07/04/2015',data_volta='18/04/2015',data_atual=d))
table.insert(dict(cidade_origem='salvador',cidade_destino='aracaju',data_saida='20/05/2015',data_volta='28/05/2015',data_atual=d))



'''
#atualizando
atual=dict(id=15,nome='lucas')
table.upsert(atual,['id'])
'''
#criando interface de usuario simple para insercao e consultas

ff=input("\nDigite -1 Agendamento /  -2 para fazer consultas:\n")

while ff == 1:
	a=input("\nCONFIRME O NUMERO PARA CADASTRAR: ")
	if a == 1:
		try:
			c_origem=raw_input("digite cidade de origem: ")
			c_destino=raw_input("digite cidade destino: ")
			d_partida=raw_input("digite a data de partida :")
			d_volta=raw_input("digite a data de volta :")

			table.insert(dict(cidade_origem=c_origem,cidade_destino=c_destino,data_saida=d_partida,data_volta=d_volta,data_atual=d))
		except:
			print("cadastro nao realizado")

	else:
		print("\ncadastro com sucesso sucesso!\n")
		break
		
ff=input("\nDigite -1 Agendamento /  -2 para fazer consultas:\n")

while ff ==2:
	a=input("\nCONFIRME O NUMERO PARA PESQUISA: ")
	print("\n")
	if a == 2:
		try:
			print("\nPESQUISAS\n")
			c_destino=raw_input("digite a cidade a ser pesquisada: ")
			get= table.find_one(cidade_destino=c_destino)
			print(get)

		except:
			print("pesquisa nao realizada!")

	else:
		print("\npesquisa feita com sucesso!\n")
		break
			




print("LISTA DE TODOS OS USUARIO CADASTRADO NO BANCO E ARQUIVO JSON DE SAIDA")
# consultando todos nomes e quantidade das pessoas e seus respectivo genero dentro do banco
result = db.query('SELECT cidade_origem, COUNT(*) c FROM city GROUP BY cidade_origem')
for row in result:
   print(row['cidade_origem'], row['c'])


# imprimindo o resultado em formato JSON
resultado=db['city'].all()
dataset.freeze(resultado,format='json',filename='city.json')

'''
#retorna um statement informando se determinada pessoa existe no banco
table = db['usuario'].table
statement = table.select(table.c.nome.like('%wendel%'))
resultado = db.query(statement)
print(resultado)
'''

