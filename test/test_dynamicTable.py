"""
@author: Kayque Damasceno
@created: 07/02/2023

@challenges: Dynamic row table
"""

import pytest
from playwright.sync_api import Page
from pages.dynamicTablePage import dynamicTablePage

def test_dynamictable(page: Page):

    dynamic_page = dynamicTablePage(page)

    dynamic_page.navigate()

    superhero_values = dynamic_page.get_superhero_information("Spider-man")

    assert superhero_values["real_name"] == "Peter Parker"