import sqlite3

connection = sqlite3.connect('tutorialBD2.db')
c= connection.cursor()

sql = 'SELECT * FROM dados WHERE keyword = ?'
sql2 = 'SELECT * FROM dados WHERE keyword =? and value = ?'

def ler_dados(leitura):
	for linha in c.execute(sql, (leitura,)):
		print(linha)

	print("=========")	

'''
	for linha in c.execute(sql2, ('python e incrivel', 5)):
		print(linha)
'''
  

ler_dados('python e incrivel')		
