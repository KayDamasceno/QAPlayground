"""
@author: Kayque Damasceno
@created: 11/02/2023

@challenges: nested Iframes
"""

import pytest
from playwright.sync_api import *
from pages.iframePage import iframePage


def test_succeed_message_is_displayed(page : Page):

    frame = iframePage(page)
    frame.navigate()

    button = page.frame_locator("#frame1").frame_locator("#frame2").locator("text='Click Me'")
    msg = page.frame_locator("#frame1").frame_locator("#frame2").locator("[id = 'msg']")

    button.click()

    expect(msg).to_be_visible()
    