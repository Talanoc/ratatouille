# -*- coding: utf-8 -*-
"""
Created on Mon Nov  9 15:38:38 2020

@author: 33633
"""
import mysql.connector
from constants import (db_name,categories)



db = mysql.connector.connect(
    host="localhost",
    user="root",
    password=""
    )
# créer un curseur de base de données pour effectuer des opérations SQL
cur = db.cursor()
cur.execute("USE" + db_name)
search_url = "https://fr.openfoodfacts.org/cgi/search.pl?"
headers = {"User-Agent": "P5_PurBeurre - Version 1.0"}


# def first_display():
# first menu 
print("***************************************************************"),
print(""),
print(" 0 : Exit "),
print(""),
print(" 1 : Change product "),
print(""),
print(" 2 : History "),
print(""),
print(" 3 : Options "),
print(""),
print("***************************************************************"),
choice=input("What do you want to do : ")


# def category_display():
# printing the categories list using loop
print("***************************************************************"),
for x in range(len(categories)):
    print(""),
    print(x, categories[x]),
print(""),
print ((x+1),"Exit"),
print(""),
print("***************************************************************"),
choice = int(input("your choice ? :"))

# def product_display():
# affichage 
cur.execute('SELECT * FROM category_product')
result = (cur.fetchall()[choice])
cur.execute('SELECT * FROM category_product')
result1 = (cur.fetchall()[choice-1])
end= result[1]
start= (result1[1])

for x in range(start, end):
    cur.execute('SELECT * FROM db_product')
    result = (cur.fetchall()[x])
    print(result[0],result[1],result[4])
db.commit()



