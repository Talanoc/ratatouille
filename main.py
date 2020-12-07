# -*- coding: utf-8 -*-
"""
Created on Fri Oct 30 23:05:30 2020

@author: 33633
"""

from database import Database
from display import Menus


def main():

    ratatouille_db = Database()
    ratatouille = Menus()

    try:
        ratatouille_db.connect()

    except:
        ratatouille_db.create_db()
        ratatouille_db.insert_category()
        print("La base est en cours de chargement")
        ratatouille_db.insert_product()
        ratatouille.first_display()

    else:
        ratatouille.first_display()


if __name__ == '__main__':

    main()
