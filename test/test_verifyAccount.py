"""
@author: Kayque Damasceno
@created: 07/02/2023

@challenges: Verify Account
"""

import pytest
from playwright.sync_api import *
from pages.verifyAccout import verifyAccount

def test_verify_with_key(page: Page):

    account_page = verifyAccount(page)

    account_page.navigate()

    numbers_to_type = page.locator("[type='number']")

    for i in range(0, numbers_to_type.count()):

        numbers_to_type.nth(i).click()

        for i in range (0, 10):
            page.keyboard.press('ArrowUp')


    expect(page.locator("[class='info success']")).to_be_visible()



def test_verify_typing(page: Page):

    account_page = verifyAccount(page)

    account_page.navigate()

    numbers_to_type = page.locator("[type='number']")

    for i in range(0, numbers_to_type.count()):

        numbers_to_type.nth(i).type('9')


    expect(page.locator("[class='info success']")).to_be_visible()


def test_wrong_input(page: Page):

    account_page = verifyAccount(page)

    account_page.navigate()

    numbers_to_type = page.locator("[type='number']")

    for i in range(0, numbers_to_type.count()):

        numbers_to_type.nth(i).type('4')

    expect(page.locator("[class='info success']")).to_be_hidden()

