# -*- coding: utf-8 -*-

############################
# projet Open Rating       #
# author: vl@cinequant.com #
############################

import re
import MySQLdb
import codecs
import os
import time
from datetime import date
from datetime import timedelta


############################
#debut du script pour creer le fichier javascript à partir de la db #
############################

db=MySQLdb.connect("localhost","cqproj","cqproj", "cqdata", use_unicode=True,charset="utf8")
c=db.cursor()

file=open ('static/open-rating/open_rating_data.js','w')
print "debut du script pour générer le fichier js à partir de la db pour open rating"

query="""SHOW COLUMNS FROM `openRating_pays`"""
c.execute(query)
results=c.fetchall()
columns=[r[0] for r in results]
columns=columns[3:]
print columns

query="""SELECT * FROM `openRating_pays`""" 	
c.execute(query)
results=c.fetchall()
file.write("/* fichier js contenant les données macro sur les pays */ \n")
text="macro=new Array();\n"
for pays in results:
	#print pays
	pays_string=str(pays[2].encode('utf8'))
	text=text+"macro['"+pays_string+"']=new Array();\n"	
	for col in columns:
	
		data=pays[columns.index(col)+3]
		print data
		text=text+"macro['"+pays_string+"']['"+str(col)+"']="
		text=text+str(data)+";\n"
	text=text[:-1]+";\n"
	

file.write(text)
file.close()
db.close()

print "fin du script"
