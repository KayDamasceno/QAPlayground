"""
@author: Kayque Damasceno
@created: 11/02/2023

@challenges: multidropdown
"""

import pytest
from playwright.sync_api import *
from pages.multilevelDropdownPage import multilevelDropdownpage

def test_if_all_icons_are_visible(page : Page):

    mld = multilevelDropdownpage(page)
    mld.navigate()


    icons = page.locator("ul li")

    expect(icons).to_have_count(4)


def test_check_settings_options(page : Page):

    mld = multilevelDropdownpage(page)
    mld.navigate()

    page.locator("ul li").last.click()
    page.locator("[href= '#settings']").click()

    settings = page.locator("[class= 'menu-item']")

    expect(settings).to_have_count(5)
    expect(settings.nth(0)).to_have_text("My Tutorial")
    expect(settings.nth(1)).to_have_text("HTML")
    expect(settings.nth(2)).to_have_text("CSS")
    expect(settings.nth(3)).to_have_text("JavaScript")
    expect(settings.nth(4)).to_have_text("Awesome!")


def test_check_animals_options(page : Page):

    mld = multilevelDropdownpage(page)
    mld.navigate()

    page.locator("ul li").last.click()
    page.locator("[href= '#animals']").click()

    settings = page.locator("[class= 'menu-item']")

    expect(settings).to_have_count(5)
    expect(settings.nth(0)).to_contain_text("Animals")
    expect(settings.nth(1)).to_contain_text("Kangaroo")
    expect(settings.nth(2)).to_contain_text("Frog")
    expect(settings.nth(3)).to_contain_text("Horse")
    expect(settings.nth(4)).to_contain_text("Hedgehog")



    

