Documentation pour Open Rating
auteur : vl@cinequant.com

architecture globale :
- 1 page web dynamique (1 fichier html index.html, 1 feuille de style "style.css" et un fichier js : openRating.js)
dans cette page, l'utilisateur rentre/valide des input dans un formulaire, qui est soumis en AJAX au serveur (voir web service ci-dessous)

- 1 webservice : dans l'archi Django : dans le view, test si des data POST sont envoyées. Dans ce cas, cela veut dire qu'on a affaire à 


Algo utilisé pour noter :
L'algo est proche du DSF du FMI.

Variables utilisées pour noter :

pays
inflation
interet
dette_PIB
defaut_exterieur
revenus
chomage
hdi : indice de développement humain

réglages de l'utilisateur
reg_credibilite
reg_macro
reg_risque
reg_dev

variables macro :
deficit_2012
deficit_2013
deficit_2014
deficit_2015
deficit_2016 : valable pour 2016 et ensuite
 
croissance_2012
croissance_2013
croissance_2014
croissance_2015
croissance_2016 : valable pour 2016 et ensuite
