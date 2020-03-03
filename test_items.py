class TestAddGoodToBasketButton:
    def test_button_add_good_in_the_basket_exist_in_page(self, browser):
        browser.get('http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/')
        browser.implicitly_wait(2)
        button = browser.find_element_by_css_selector('.btn-add-to-basket')
        assert button is not None
