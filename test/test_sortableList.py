"""
@author: Kayque Damasceno
@created: 11/02/2023

@challenges: sortable list with Drag and Drop
"""

import pytest
from playwright.sync_api import *
from pages.sortableListPage import sortableList


def test_check_list_in_gree(page : Page):

    spage = sortableList(page)
    spage.navigate()

    rows = page.locator("ul li")

    page.locator("[id='check']").click()

    for i in range(0, rows.count()):

        name = rows.nth(i)
        is_green = True

        if name.get_attribute("class") == "wrong":
             is_green = False


        print(is_green)
        
