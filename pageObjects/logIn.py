from selenium.webdriver.common.by import By


class LogIn:
    def __init__(self, driver):
        self.signup_link = (By.XPATH, "//a[normalize-space()='Sign Up']")
        self.driver = driver

    def go_to_signup(self):
        self.driver.find_element(*self.signup_link).click()
