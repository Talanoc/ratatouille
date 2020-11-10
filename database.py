# -*- coding: utf-8 -*-
"""
Created on Thu Oct 29 23:55:59 2020

@author: 33633
"""

import mysql.connector
from constants import db_name


# connexion à la base de données
db = mysql.connector.connect(
    host="localhost",
    user="root",
    password=""
    )

# créer un curseur de base de données pour effectuer des opérations SQL
cur = db.cursor()
cur.execute("DROP DATABASE IF EXISTS" + db_name)
# exécuter le curseur avec la méthode execute() et transmis la requête SQL
cur.execute("CREATE DATABASE IF NOT EXISTS" + db_name)
cur.execute("USE" + db_name)

cur.execute("""
            CREATE TABLE IF NOT EXISTS db_product (
    id SMALLINT UNSIGNED NOT NULL AUTO_INCREMENT,
    product_name_fr VARCHAR(100) NOT NULL DEFAULT 'N/A',
    code VARCHAR(13) ,
    brands VARCHAR(100) NOT NULL DEFAULT 'N/A',
    url VARCHAR(150) NOT NULL DEFAULT 'N/A',
    nutrition_grades CHAR(1) NOT NULL DEFAULT 'x',
    stores VARCHAR(200) NOT NULL DEFAULT 'N/A',
    PRIMARY KEY(id)
);
""")

cur.execute("""
            CREATE TABLE IF NOT EXISTS owner_product (
    id SMALLINT UNSIGNED NOT NULL,
    product_name_fr VARCHAR(100) NOT NULL,
    code VARCHAR(13) NOT NULL UNIQUE,
    brands VARCHAR(100) NOT NULL,
    url VARCHAR(150) NOT NULL,
    nutri_grades CHAR(1) NOT NULL,
    stores VARCHAR(100),
    date_creation TIMESTAMP NULL DEFAULT CURRENT_TIMESTAMP ,
    PRIMARY KEY(id)
);
""")

cur.execute("""
            CREATE TABLE IF NOT EXISTS history_product (
    id SMALLINT UNSIGNED NOT NULL,
    product_name_fr VARCHAR(100) NOT NULL,
    old_id SMALLINT UNSIGNED NOT NULL,
    old_product_name_fr VARCHAR(100) NOT NULL,
    date_creation TIMESTAMP NULL DEFAULT CURRENT_TIMESTAMP ,
    PRIMARY KEY(id)
);
""")


cur.execute("""
            CREATE TABLE IF NOT EXISTS category_product (
    category VARCHAR(100) NOT NULL,
    last_index_category SMALLINT UNSIGNED NOT NULL

);
""")
