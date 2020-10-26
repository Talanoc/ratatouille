# -*- coding: utf-8 -*-
"""
Created on Wed Oct 21 15:12:29 2020

@author: 33633
"""


import mysql.connector
import requests
from constants import categories,chosen_fields
x=str
q=0
r=0
#connexion à la base de données
"""

#créer un curseur de base de données pour effectuer des opérations SQL
cur = db.cursor()
#exécuter le curseur avec la méthode execute() et transmis la requête SQL
#cur.execute("CREATE DATABASE ratatouille")
"""

db = mysql.connector.connect(
    host = "localhost",
    user = "root",
    password = "Simon2311",
    database = "ratatouille")

cur = db.cursor()
search_url="https://fr.openfoodfacts.org/cgi/search.pl?"
headers = {"User-Agent": "P5_PurBeurre - Version 1.0"}
json_category_product={}

for category in categories:
    q=0
    i=1
    products_resu =[]
    for i in range (1,2):
        payload={"action": "process",
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
                    "page_size":30,
                    "json": True
                    }
        req=requests.get(search_url,params=payload,headers=headers)        
        results_json=req.json()       
        products_json=results_json["products"]
                                  
        for product in products_json:
            
            product_resu = {
                        key : value for key, value in product.items()
                        if key in chosen_fields 
                     }
            q=q+1
            
            print ("**************************************************")
            print (q,"****",product_resu)
            print ("**************************************************")
            
"""           
            for key,value in product_resu.items():
                                
                if len(product_resu) == len(chosen_fields):                
                    products_resu.append(product_resu)
                    q +=1
                    print("******************************")
                    print (key,':',value)
                    print ("*******",q,":",category,"n°",int(i/10),"********")
"""                    
                    
                    
"""                   
                    q +=1
                    print("******************************")
                    print (key,':',value)
                    print ("*******",q,":",category,"n°",int(i/10),"********")
            #print()
            
            #print(" Catégorie '{}': {} produits importés de l'API Open Food Facts{} \n" \
                   # .format(category, q,chosen_fields[0]))
            json_category_product[category] = products_resu
""" 
"""           
            q=q+1    
            print(len(products_resu),q)
            print (product_resu.get("url"))
            print (product_resu.get("brands"))
            print (product_resu.get("product_name_fr"))
            print (product_resu.get("nutrition_grades"))


"""            
           
                