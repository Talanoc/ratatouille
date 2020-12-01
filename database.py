# -*- coding: utf-8 -*-
"""
Created on Fri Nov 13 14:36:32 2020

@author: 33633
"""
import mysql.connector
from constants import *
import requests


class Database:

    def __init__(self):
        self.db_name = db_name
        self.table = table
        

    def connect(self):
        self.con()
        self.cur.execute("USE" + self.db_name)

    def con(self):
        self.db = mysql.connector.connect(host="localhost",
                                          user="root", password="")
        self.cur=self.db.cursor()

    def destruct_db(self):

        self.con()
        self.cur.execute("DROP DATABASE IF EXISTS" + self.db_name)

    def create_db(self):

        self.con()
        self.cur.execute("CREATE DATABASE IF NOT EXISTS" + self.db_name)
        self.cur.execute("USE" + self.db_name)

        for table in self.table:
            self.cur.execute(table)

    def use_db(self):
        
        self.categories = categories
        self.connect()


    def insert_category(self):

        self.use_db()
        for n in range (len((self.categories))):
            cat=self.categories[n]
            self.cur.execute("INSERT INTO category_product(category) VALUES "\
                        "('"+cat+"')")
            self.db.commit()

    def insert_product(self):

        self.categories = categories
        self.connect()

        search_url = "https://fr.openfoodfacts.org/cgi/search.pl?"
        headers = {"User-Agent": "P5_PurBeurre - Version 1.0"}

        for category in self.categories:

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
                           "page": 1,
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

                        x=product_resu["categories"]
                        for i,cat in enumerate(self.categories):
                            if cat in x:
                                product_resu["categories"]=i+1

                        self.cur.execute("""INSERT INTO db_product (product_name_fr,category,
                                    code,brands,url,nutrition_grades,stores
                                    ) VALUES (%(product_name_fr)s,(%(categories)s),
                                    %(code)s,%(brands)s,%(url)s,%(nutrition_grades)s,%(stores)s)""", product_resu)

                        self.db.commit()

