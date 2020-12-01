# -*- coding: utf-8 -*-
"""
Created on Mon Nov  9 15:38:38 2020

@author: 33633
"""

import mysql.connector
from constants import *
from database import Database
import random
import sys

choice = 0
x = 0


class Menus(Database):

    def __init__(self):

        self.choice = choice
        self.db_name = db_name

    def first_display(self):

        print(ligne)
        print(bienvenue)
        print(ligne)
        print("")
        print(" 0 : Exit ")
        print("")
        print(" 1 : Change product ")
        print("")
        print(" 2 : History ")
        print("")
        print(" 3 : Réinitialiser les bases de données ")
        print("")
        print(ligne)

        self.choice = int(input("What do you want to do ? : "))

        if self.choice == 0:
            print("Au revoir")
            sys.exit()

        elif self.choice == 1:
            self.change_product()

        elif self.choice == 2:
            self.history_display()

        elif self.choice == 3:
            self.destruct_db()
            print("La base de données est effaçée")
            sys.exit()

    def change_product(self):

        self.category_display()
        self.product_display()
        self.good_choice()
        self.nutri_test()
        self.first_display()

    def category_display(self):

        # printing the categories list using loop
        print(ligne)
        print(display_cat)
        print(ligne)
        
        for x in range(len(categories)):
            print("")
            print(x+1, categories[x])
        print("")
        print((x+2), "Retour au menu précédent")
        print("")
        print(ligne)

        self.choice = int(input("Quelle categorie ? :"))

        if self.choice >= int(len(categories)+1):
            print("!!!! Entrée n'appartenant à la liste.Retour au\
                  départ  !!!!")
            self.first_display()
        else:
            self.cat =str(self.choice)

    def product_display(self):

        x = 0
        self.connect()
        self.cur.execute('SELECT id,category,product_name_fr,nutrition_grades\
                         FROM db_product where category ='+ self.cat)
        result = (self.cur.fetchall())
        
# random generation of the product to be replaced
        self.origin_product = (random.choice(result))
        
# display of the product to be replaced
        print(ligne)
        print(replace)
        print(ligne)

        print(self.origin_product)
# display of the replacement list
        print(ligne)
        print(replace_choice)
        print(ligne)

        for x in range(len(result)):
            print(result[x])

        print(ligne)
# replacement product entry
        self.choice = str(input("produit de remplacement? :"))
# loading of the data corresponding to the product replace
        self.cur.execute('SELECT id,category,product_name_fr,nutrition_grades \
                         FROM db_product where id ='+self.choice)
        self.replace_product = (self.cur.fetchone())
        
        print(ligne)
        print("produit de départ", self.origin_product)
        print("produit de remplacement :", self.replace_product)
        print(ligne)

    def good_choice(self):

        self.connect()
        if self.origin_product[1] == self.replace_product[1] and\
                self.origin_product[0] != self.replace_product[0]:
# product in the same category 
            self.user = (self.origin_product[0], self.replace_product[0])

        else:
# product not belonging to the same category
            print(ligne)
            print(error1)
            print(ligne)
            self.choice = str(input("produit de remplacement? :"))
            self.cur.execute('SELECT id,category,product_name_fr,\
                        nutrition_grades FROM db_product where id ='+self.choice)
            self.replace_product = (self.cur.fetchone())
            self.good_choice()

    def nutri_test(self):

        user=(self.origin_product[0],self.replace_product[0])
        self.connect()

        if nutri_list.index(self.origin_product[3]) >=\
                nutri_list.index(self.replace_product[3]):
            print("*****     Echange enregistré              *****")
            self.cur.execute("""INSERT INTO history_product(product_id,replace_id)\
                             VALUES (%s,%s)""", user)
            self.db.commit()
            self.first_display()
        else:
            print(ligne)
            print(error2)
            print(ligne)

            self.choice = str(input("Sauvegarder quand même (Y/N) ? :"))

            if self.choice == "y" or self.choice == "Y":
                self.cur.execute("""INSERT INTO history_product (product_id,replace_id)\
                                 VALUES (%s,%s)""", user)
                self.db.commit()

            elif self.choice == "n" or self.choice == "N":
                pass

            else:
                print("Il faut répondre par Y ou N ")
                #self.first_display()

    def product_choice(self):
        self.connect()

        self.choice = str(input("produit de remplacement? :"))
        self.cur.execute('SELECT id,category,product_name_fr,nutrition_grades\
                         FROM db_product where id ='+self.choice)
        self.replace_product = (self.cur.fetchone())

    def history_display(self):

        self.connect()
        self.cur.execute('SELECT * FROM history_product')
        self.history_product = (self.cur.fetchall())
        print("Historique des mouvements:")
        for index, start, end, date in self.history_product:
            print(ligne1)
            print("Date de changement:", date)
            print(ligne1)
            self.cur.execute('SELECT product_name_fr,brands,nutrition_grades,url\
                             FROM db_product where id =' + start)
            start_product = (self.cur.fetchall())
            print("produit de départ:")
            print(ligne1)
            print(start_product)
            print(ligne1)

            self.cur.execute('SELECT product_name_fr,brands,nutrition_grades,url\
                             FROM db_product where id =' + end)

            end_product=(self.cur.fetchall())
            print("produit de remplacement:")
            print(ligne1)
            print(end_product)
            print(ligne1)
        self.first_display()

