"""
@author: Kayque Damasceno
@created: 11/02/2023

@challenges: handling pop ups
"""

import pytest
from playwright.sync_api import *
from pages.popupPage import popupPage


def test_pop_up_message(page : Page):

    popup = popupPage(page)
    popup.navigate()

    with page.expect_popup() as info:
        page.locator("#login").click()

    pop = info.value
    expect(pop.locator("[type='button']")).to_have_text("Submit")


    