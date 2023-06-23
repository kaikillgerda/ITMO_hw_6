from pages.swag_labs import SwagLabs
from pages.base_page import BasePage

def test_check_icon(browser):
    icon = SwagLabs(browser)
    field = BasePage(browser)
    icon.visit()
    assert icon.exist_icon
    assert field.find_element('#user-name')
    assert field.find_element('#password')
