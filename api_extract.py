# -*- coding: utf-8 -*-
"""
Created on Wed Oct 21 15:12:29 2020

@author: 33633
"""


import mysql.connector
import requests
from constants import categories, chosen_fields, db_name, qty_prod

z = 0
r = 0
last_index_category=0
qte = []

#def filling_db():
    # connexion à la base de données
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

for category in categories:
    q = 0
    i = 1
    products_resu = []
    for i in range(1, 2):
        payload = {"action": "process",
                   "tagtype_0": "categories",
                   "tag_contains_0": "contains",
                   "tag_0": category,
                   "tagtype_1": "countries",
                   "tag_contains_1": "contains",
                   "tag_1": "france",
                   "tagtype_2": "categories_lc",
                   "tag_contains_2": "contains",
                   "tag_2": "fr",
                   # Sort by popularity
                   "sort_by": "unique_scans_n",
                   "page": i,
                   "page_size": qty_prod,
                   "json": True}
       
        req = requests.get(search_url, params=payload, headers=headers)
        
        results_json = req.json()
        products_json = results_json["products"]
     
        for product in products_json:

            product_resu = {
                        key: value for key, value in product.items()
                        if key in chosen_fields and value != " "
                     }
            
            if len(product_resu) == len(chosen_fields):
             
                cur.execute("""INSERT INTO db_product (product_name_fr,
                            code,brands,url,nutrition_grades,stores
                            ) VALUES (%(product_name_fr)s,
                            %(code)s,%(brands)s,%(url)s,%(nutrition_grades)s,%(stores)s)""",product_resu)
                last_index_category=last_index_category + 1
                db.commit()
                print ("La base de données comprend",last_index_category,"articles")

                cat = (category, last_index_category)
    cur.execute("""INSERT INTO category_product (category, last_index_category  ) VALUES(%s, %s)""", cat)
    db.commit()
    cat= ("debut",1)
cur.execute("""INSERT INTO category_product (category, last_index_category  ) VALUES(%s, %s)""", cat)
db.commit()                

'''

# ---affichage d'une categorie---#
#def category_display():

z = int(input("quelle category ?:"))
cur.execute('SELECT * FROM category_product')
result = (cur.fetchall()[z])
cur.execute('SELECT * FROM category_product')
result1 = (cur.fetchall()[z-1])
end= result[1]
start= (result1[1] - 1)
print (start)
print (end)

for x in range(start, end):
    cur.execute('SELECT * FROM db_product')
    result = (cur.fetchall()[x])
    print(result[0],result[1],result[3],result[4])
db.commit()


# ---selection et sauvegarde d'un produit dans owner_product---#

y = int(input("quel produit voulez-vous ajouter à votre selection :"))

if y != 0:
    cur.execute('SELECT * FROM db_product')
    result = (cur.fetchall()[y])
    print(result)
    cur.execute("""INSERT INTO owner_product (id,product_name_fr,code,brands,url,nutri_grades,
                stores) VALUES (%s,%s,%s,
                %s,%s,%s,%s)""", result)



y = int(input("quel produit voulez-vous ajouter à votre selection :"))
0
if y != 0:
    cur.execute('SELECT * FROM db_product')
    result = (cur.fetchall()[y])
    print(result)
    cur.execute("""INSERT INTO owner_product (id,product_name_fr,code,brands,url,nutri_grades,
                stores) VALUES (%s,%s,%s,
                %s,%s,%s,%s)""", result)

db.commit()
'''