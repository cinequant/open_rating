# -*- coding: utf-8 -*-

############################
# Open Ratin               #
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
#debut du script
############################

db=MySQLdb.connect("localhost","cqproj","cqproj", "cqdata", use_unicode=True,charset="utf8")
c=db.cursor()

#os.environ['DJANGO_SETTINGS_MODULE'] = 'cqsite.settings'
#from models import Pays

print "debut du script pour recuperer les donnees du WEO et les mettre dans la db qui va bien pour open Rating"
#raw_input("Press Enter to continue...")
#pays_list = Pays.objects.all()
query="""SELECT `nom`,`weo` FROM `openRating_pays`""" 	
c.execute(query)
results=c.fetchall()
for pays in results:
	weo=int(pays[1])
	query="""SELECT `2011` FROM `WEO` WHERE `WEO Country Code` = '"""+str(weo)+ """' AND `Subject Descriptor`= 'Unemployment rate'"""
	c.execute(query)
	resultsWEO=c.fetchall()
	chomage=float(resultsWEO[0][0].replace(',',''))
	print chomage

	query="""SELECT `2011` FROM `WEO` WHERE `WEO Country Code` = '"""+str(weo)+ """' AND `Subject Descriptor`= 'Gross domestic product, constant prices' AND `Units`='Percent change'"""
	c.execute(query)
        resultsWEO=c.fetchall()
	croissance=float(resultsWEO[0][0].replace(',',''))
        print croissance

	query="""SELECT `2012`,`2013`,`2014`,`2015`,`2016` FROM `WEO` WHERE `WEO Country Code` = '"""+str(weo)+ """' AND `Subject Descriptor`= 'Gross domestic product, constant prices' AND `Units`='Percent change'"""
	c.execute(query)
        resultsWEO=c.fetchall()
	print resultsWEO
	croissance_2012=float(resultsWEO[0][0].replace(',',''))
	croissance_2013=float(resultsWEO[0][1].replace(',',''))
	croissance_2014=float(resultsWEO[0][2].replace(',',''))
	croissance_2015=float(resultsWEO[0][3].replace(',',''))
	croissance_2016=float(resultsWEO[0][4].replace(',',''))

	query="""SELECT `2011`,`2012`,`2013`,`2014`,`2015`,`2016` FROM `WEO` WHERE `WEO Country Code` = '"""+str(weo)+ """' AND `Subject Descriptor`= 'General government total expenditure' AND `Units`='Percent of GDP'"""
	c.execute(query)
        resultsWEO=c.fetchall()
	print resultsWEO
	depenses_2011=float(resultsWEO[0][0].replace(',',''))
	depenses_2012=float(resultsWEO[0][1].replace(',',''))
	depenses_2013=float(resultsWEO[0][2].replace(',',''))
	depenses_2014=float(resultsWEO[0][3].replace(',',''))
	depenses_2015=float(resultsWEO[0][4].replace(',',''))
	depenses_2016=float(resultsWEO[0][5].replace(',',''))

	query="""SELECT `2011`,`2012`,`2013`,`2014`,`2015`,`2016` FROM `WEO` WHERE `WEO Country Code` = '"""+str(weo)+ """' AND `Subject Descriptor`= 'General government revenue' AND `Units`='Percent of GDP'"""
        c.execute(query)
        resultsWEO=c.fetchall()
        print resultsWEO
        recettes_2011=float(resultsWEO[0][0].replace(',',''))
	recettes_2012=float(resultsWEO[0][1].replace(',',''))
        recettes_2013=float(resultsWEO[0][2].replace(',',''))
        recettes_2014=float(resultsWEO[0][3].replace(',',''))
        recettes_2015=float(resultsWEO[0][4].replace(',',''))
	recettes_2016=float(resultsWEO[0][5].replace(',',''))

	deficit_2011=-recettes_2011+depenses_2011
	deficit_2012=-recettes_2012+depenses_2012
	deficit_2013=-recettes_2013+depenses_2013
	deficit_2014=-recettes_2014+depenses_2014
	deficit_2015=-recettes_2015+depenses_2015
	deficit_2016=-recettes_2016+depenses_2016

	query="""SELECT `2011` FROM `WEO` WHERE `WEO Country Code` = '"""+str(weo)+ """' AND `Subject Descriptor`= 'Gross domestic product per capita, current prices' AND `Units`='U.S. dollars'"""
	c.execute(query)
        resultsWEO=c.fetchall()
        revenus=float(resultsWEO[0][0].replace(',',''))
	print revenus

	query="""SELECT `2011` FROM `WEO` WHERE `WEO Country Code` = '"""+str(weo)+ """' AND `Subject Descriptor`= 'General government gross debt' AND `Units`='Percent of GDP'"""
	c.execute(query)
        resultsWEO=c.fetchall()
        dette=float(resultsWEO[0][0].replace(',',''))
	print dette

	query="""SELECT `2011` FROM `WEO` WHERE `WEO Country Code` = '"""+str(weo)+ """' AND `Subject Descriptor`= 'Current account balance' AND `Units`='Percent of GDP'"""
        c.execute(query)
        resultsWEO=c.fetchall()
        courant=float(resultsWEO[0][0].replace(',',''))

	print pays

	#on met tout cela dans la db utilisee pour open rating
	query="""UPDATE `cqdata`.`openRating_pays` SET `chomage` =  '%(a0)s', `croissance`='%(a1)s',`revenus`='%(a2)s',`dette_PIB`='%(a3)s',`bop`='%(a4)s',`croissance_2012`='%(a5)s',`croissance_2013`='%(a6)s',`croissance_2014`='%(a7)s',`croissance_2015`='%(a8)s',`croissance_2016`='%(a9)s',`deficit_PIB`='%(d1)s',`deficit_2012`='%(d2)s',`deficit_2013`='%(d3)s',`deficit_2014`='%(d4)s',`deficit_2015`='%(d5)s',`deficit_2016`='%(d6)s' WHERE `openRating_pays`.`WEO` ='%(a10)s';""" % {'a0':chomage,'a1':croissance,'a2':revenus,'a3':dette,'a4':courant,'a5':croissance_2012,'a6':croissance_2013,'a7':croissance_2014,'a8':croissance_2015,'a9':croissance_2016,'a10':weo,'d1':deficit_2011,'d2':deficit_2012,'d3':deficit_2013,'d4':deficit_2014,'d5':deficit_2015,'d6':deficit_2016} 
        c.execute(query)

db.close()

print "fin du script"
