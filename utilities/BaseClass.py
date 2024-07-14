from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import TimeoutException


class BaseClass:
    def wait_for_element_visible(self, by, value, timeout=40):
        try:
            return WebDriverWait(self.driver, timeout).until(
                EC.visibility_of_element_located((by, value))
            )
        except TimeoutException:
            print(f"Element with {by} = {value} not visible after {timeout} seconds.")
            return None

    def wait_for_element_clickable(self, by, value, timeout=30):
        try:
            return WebDriverWait(self.driver, timeout).until(
                EC.element_to_be_clickable((by, value))
            )
        except TimeoutException:
            print(f"Element with {by} = {value} not clickable after {timeout} seconds.")
            return None

    def wait_for_url_change(self, old_url, timeout=20):
        try:
            WebDriverWait(self.driver, timeout).until(EC.url_changes(old_url))
        except TimeoutException:
            print(f"URL did not change from {old_url} after {timeout} seconds.")

    def wait_for_title_contains(self, title, timeout=20):
        try:
            WebDriverWait(self.driver, timeout).until(
                EC.title_contains(title)
            )
        except TimeoutException:
            print(f"Title does not contain '{title}' after {timeout} seconds.")
