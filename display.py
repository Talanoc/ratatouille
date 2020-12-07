# -*- coding: utf-8 -*-
"""
Created on Mon Nov  9 15:38:38 2020

@author: 33633
"""

# import mysql.connector
from constants import ligne, ligne1, error1, db_name, bienvenue,\
    display_cat, categories, replace, replace_choice, nutri_list
from database import Database
import sys
# from os import system
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

        self.choice = int(input("Que voulez-vous faire ? : "))

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
        else:
            print("!!!!!      Choix invalide                 !!!!!!!!")
            self.first_display()
    def change_product(self):
        """
        Program run if the choice of first_display is 1.

        Returns
        -------
        None.

        """
        self.category_display()
        self.product_display()
        self.replace_display()
        self.good_choice()
        self.nutri_test()
        self.first_display()

    def category_display(self):
        """
        Display of category list & category select.

        -------
        Selection of category number.
        The selected number is placed in the variable self.cat.
        """
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
            print("!!!! Entrée n'appartenant à la liste.Retour au départ  !!!!")
            self.first_display()
        else:
            self.cat = str(self.choice)

    def product_display(self):
        """
        Display of the list of products in the category.& product select.

        -------
        Selection of a product in the list.
        The selected number is placed in the variable self.origin_product.
        """
        x = 0
        self.connect()
        self.cur.execute('SELECT id,category_id,product_name_fr,nutrition_grades\
                         FROM db_product where category_id =' + self.cat)
        self.result = (self.cur.fetchall())

        print(ligne)
        print(replace)
        print(ligne)
        for x in range(len(self.result)):
            print(self.result[x])
        print(ligne)
        print(ligne1)

        self.origin_product = (input("Quelle produit voulez vous remplacer ? :"))

        self.cur.execute('SELECT id,category_id,product_name_fr,nutrition_grades\
                         FROM db_product where id =' + self.origin_product)
        self.origin_product = (self.cur.fetchone())
        
        if int(self.origin_product[1]) != int(self.cat):
            print("!!!!          Choix n'appartenant pas à la liste    !!!!!")
            self.product_display()
        else:
            pass


    def replace_display(self):
        """
        Display of the list of products with a better nutriscore & \
            product select.

        -------
        Selection of a product in the list.
        The selected number is placed in the variable self.replace_product.
        """
        print(ligne)
        print(replace_choice)
        print(ligne)

        a = 0
        for x in range(len(self.result)):
            self.replace_choice = self.result[x]
            if nutri_list.index(self.origin_product[3]) >\
                    nutri_list.index(self.replace_choice[3]):
                a += 1
                print(self.replace_choice)

        if a == 0:
            print(ligne1)
            print("Pas de produits ayant un meilleur nutriscore")
            print(ligne1)
            self.first_display()
# replacement product entry
        self.choice = str(input("produit de substitution ? :"))

# loading of the data corresponding to the product replace
        self.cur.execute('SELECT id,category_id,product_name_fr,nutrition_grades \
                         FROM db_product where id ='+self.choice)
        self.replace_product = (self.cur.fetchone())
        self.result_display()

    def result_display(self):
        """
        Display of the starting product and the exchanged one.

        -------
        None.
        """
        print(ligne)
        print("produit de départ", self.origin_product)
        print("produit de remplacement :", self.replace_product)
        print(ligne)

    def good_choice(self):
        """
        Check if the product is part of the category and if the product is\
            different from the starting product.

        -------
        Creation of the self.user list.
        """
        self.connect()
        if self.origin_product[1] == self.replace_product[1] and\
                self.origin_product[0] != self.replace_product[0]:

            self.user = (self.origin_product[0], self.replace_product[0])

        else:

            print(ligne)
            print(error1)
            print(ligne)
            self.choice = str(input("produit de remplacement? :"))
            self.cur.execute('SELECT id,category_id,product_name_fr,\
                    nutrition_grades FROM db_product where id ='+self.choice)
            self.replace_product = (self.cur.fetchone())
            self.result_display()
            self.good_choice()

    def nutri_test(self):
        """
        Save the self.user list in the history-product table.

        -------
        None.
        """
        self.connect()

        print("*****     Echange enregistré              *****")
        self.cur.execute("""INSERT INTO history_product(product_id,\
                         replace_id) VALUES (%s,%s)""", self.user)
        self.db.commit()

    def history_display(self):
        """
        Display replacement history.

        -------
        None.
        """
        self.connect()
        self.cur.execute('SELECT * FROM history_product')
        self.history_product = (self.cur.fetchall())
        print("Historique des mouvements:")
        for index, start, end, date in self.history_product:
            print(ligne1)
            print("Date de changement:", date)
            print(ligne1)
            self.cur.execute('SELECT product_name_fr,\
                             brands,nutrition_grades,url\
                             FROM db_product where id =' + start)
            start_product = (self.cur.fetchall())
            print("produit de départ:")
            print(ligne1)
            print(start_product)
            print(ligne1)

            self.cur.execute('SELECT product_name_fr,\
                             brands,nutrition_grades,url\
                             FROM db_product where id =' + end)

            end_product = (self.cur.fetchall())
            print("produit de remplacement:")
            print(ligne1)
            print(end_product)
            print(ligne1)
        self.first_display()
