from selenium.webdriver.common.by import By

class SecurePage:
    #locators
    WELCOME_TEXT = (By.CLASS_NAME,'subheader')
    FLASH_TEXT = (By.ID, 'flash')
    LOGOUT_BUTTON = (By.CLASS_NAME, 'icon-2x icon-signout')

    # URL
    URL = 'https://the-internet.herokuapp.com/secure'

    def __init__(self, browser):
        self.browser = browser

    def get_welcome_text(self, browser):
        return self.browser.find_element(*self.WELCOME_TEXT).text

    def get_current_url(self):
       return self.browser.current_url

    def get_flash_message(self):
       return self.browser.find_element(*self.FLASH_TEXT).text

    def click_logout_button(self):
        self.browser.find_element(*self.LOGOUT_BUTTON).click

