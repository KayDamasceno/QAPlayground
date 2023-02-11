"""
@author: Kayque Damasceno
@created: 11/02/2023

@challenges: tags
"""

import pytest
from playwright.sync_api import *
from pages.tagsPage import tagsPage

words = ["They", "know", "nothing", "Jon", "Snow", "Taergaryan", "Dracarys", "Sansa", "Kingslanding", "ASOIAF"]

def test_add_tags_and_check_text(page: Page):

    tags_page = tagsPage(page)
    tags_page.navigate()
    tags_page.clean_tags()

    count = 10
    for word in words:
        text = page.locator("div p").last
        expect(text).to_contain_text(str(count)+" tags are remaining")
        tags_page.add_tag(word)
        count-=1

    text = page.locator("div p").last
    expect(text).to_contain_text("0 tags are remaining")
    

def test_remove_all(page: Page):

    tags_page = tagsPage(page)
    tags_page.navigate()
    tags_page.clean_tags()

    for word in words:
        tags_page.add_tag(word)

    
    page.locator("div button").click()

    text = page.locator("div p").last
    expect(text).to_contain_text("0 tags are remaining")
    
        
