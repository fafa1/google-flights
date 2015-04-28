

import sqlite3
import time
import datetime

connection = sqlite3.connect('tutorialBD2.db')
c=connection.cursor()

def tabela():
	c.execute('CREATE TABLE IF NOT EXISTS dados (id integer, unix real, keyword text, datstemp text, value real)') 

tabela()


def inserir():
	c.execute("INSERT INTO dados VALUES (1, 123456.5454, 'python e incrivel', '2014/04/15 10:08:59',5)")
	c.execute("INSERT INTO dados VALUES (2, 545454.545, 'python e incrivel', '2014/06/25 01:08:49', 7)")
	c.execute("INSERT INTO dados VALUES (3, 5454.54, 'python e incrivel', '2014/07/02 07:08:20',10)")
	c.execute("INSERT INTO dados VALUES (4, 545454.54,'python e incrivel', '2014/10/25 12:05:60',3)")
	c.execute("INSERT INTO dados VALUES (5, 54545454.45, 'python e incrivel','2015/06/02 11:08:20',4)")


	

	connection.commit()

inserir()	
