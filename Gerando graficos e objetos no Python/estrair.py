
'''
 USANDO SQLITE3
Funcionou pois fiz a alteracao da data de Y-m-d para Y/m/d; 
ele extrai informacao do banco de dado 'tutorialBD2.db' e gera um grafico
o arquivo estrair.py e teste.py, tem que estar no mesmo local
'''
#-*- coding: utf-8 -*-
import sqlite3
import matplotlib.pyplot as plt
import matplotlib.dates as mdates

connection = sqlite3.connect('tutorialBD2.db')
c=connection.cursor()

sql= 'SELECT * FROM dados' # guardo em sql o banco

x=[]
y=[]

conversor=mdates.strpdate2num('%Y/%m/%d %H:%M:%S')


def leitura(leitura):
   for row in c.execute(sql):
      x.append(conversor(row[3]))
      y.append(row[4])

leitura('python e incrivel')


fig=plt.figure()
ax1=fig.add_subplot(1,1,1, axisbg= 'white')
plt.plot_date(x,y, fmt='r-',label='values')
plt.legend(['values'])
plt.grid(True)
plt.show()

