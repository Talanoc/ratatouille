# -*- coding: utf-8 -*-
"""
Created on Wed Oct 21 11:09:34 2020

@author: 33633
"""

db_name = " ratatouille"

qty_prod = 15

nutri_list = ["a", "b", "c", "d", "e", "f", "g", "h"]

# ------------ Some Categories from OpenFood Facts ------------ #
categories = [
    "Eaux",
    "Poissons",
    "Viandes",
    "Jambons",
    "Desserts",
    "Plats préparés surgelés",
    "Fromages de France",
    "Bonbons",
    "Pains"
    ]

# -------- Some useful fields required for each product requested --------- #
chosen_fields = [
    "product_name_fr",
    "generic_name_fr",
    "code",
    "url",
    "brands",
    "nutrition_grades",
    "pnns_groups_1",
    "pnns_groups_2",
    "categories",
    "stores"
    ]


table_category_product = """
            CREATE TABLE IF NOT EXISTS category_product (
                       id INT AUTO_INCREMENT,
                       category VARCHAR(255),
                       PRIMARY KEY (id)
);
"""

table_db_product = """
            CREATE TABLE IF NOT EXISTS db_product (
                       id SMALLINT UNSIGNED AUTO_INCREMENT,
                       category INT,
                       code VARCHAR(13),
                       brands VARCHAR(100),
                       product_name_fr VARCHAR(200),
                       nutrition_grades CHAR(1),
                       stores VARCHAR(200),
                       url VARCHAR(300),
                       PRIMARY KEY (id),
                       CONSTRAINT fk_sub_id FOREIGN KEY (
                           category) REFERENCES category_product(id)
);
"""

table_history_product = """
            CREATE TABLE IF NOT EXISTS history_product (
                       id SMALLINT UNSIGNED AUTO_INCREMENT,
                       product_id varchar(10),
                       replace_id varchar(10),
                       date_creation TIMESTAMP NULL DEFAULT CURRENT_TIMESTAMP,
                       PRIMARY KEY(id)
);
"""

table = (table_category_product, table_db_product, table_history_product)


ligne1 = ("-----------------------------------------------------------------")
ligne = ("*************************************************************")
bienvenue = ("*****       Bienvenue sur ratatouille                   *****")
display_cat = ("*****       Dans quelle categorie ?                     *****")
replace = ("*****       Produit à remplacer:                        *****")
replace_choice = ("*****       Produits de remplacement                    *****")
error1 = ("*****      Choisir un produit dans la liste !!!!!       *****")
error2 = ("*****      Le nutriscore est moins bon !!!!!            *****")
