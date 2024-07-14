from selenium.common.exceptions import TimeoutException, NoSuchElementException
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait, Select
from selenium.webdriver.support import expected_conditions as EC


class SignUpPage:
    def __init__(self, driver):
        self.driver = driver

    def wait_for_element_visible(self, by, value, timeout=10):
        try:
            element = WebDriverWait(self.driver, timeout).until(
                EC.visibility_of_element_located((by, value))
            )
            return element
        except TimeoutException:
            print(f"Element with {by} = {value} not visible after {timeout} seconds.")
            return None

    def wait_for_element_clickable(self, by, value, timeout=10):
        try:
            element = WebDriverWait(self.driver, timeout).until(
                EC.element_to_be_clickable((by, value))
            )
            return element
        except TimeoutException:
            print(f"Element with {by} = {value} not clickable after {timeout} seconds.")
            return None

    def enter_username(self, username):
        element = self.wait_for_element_visible(By.ID,"username")
        if element:
            element.send_keys(username)

    def enter_email(self, email):
        element = self.wait_for_element_visible(By.ID, "email")
        if element:
            element.send_keys(email)

    def enter_password(self, password):
        element = self.wait_for_element_visible(By.ID, "pass")
        if element:
            element.send_keys(password)

    def enter_confirm_password(self, confirm_password):
        element = self.wait_for_element_visible(By.ID, "cpass")
        if element:
            element.send_keys(confirm_password)

    def select_gender(self, gender):
        gender_dropdown = Select(
            self.wait_for_element_visible(By.ID, "gender")
        )
        gender_dropdown.select_by_visible_text(gender)

    def submit_form(self):
        submit_button = self.wait_for_element_clickable(By.XPATH, "//input[@type='submit' and @value='Sign Up']")
        if submit_button:
            submit_button.click()

    def clear_fields(self):
        for field_id in ["username", "email", "pass", "cpass"]:
            element = self.wait_for_element_visible(By.ID, field_id)
            if element:
                element.clear()

    def is_field_displayed(self, field_id):
        element = self.wait_for_element_visible(By.ID, field_id)
        return element is not None

    def get_validation_messages(self):
        # Wait for the validation messages to be present
        validation_message_elements = WebDriverWait(self.driver, 10).until(
            EC.presence_of_all_elements_located((By.CLASS_NAME, 'error'))
        )

        # Retrieve and return the text of each validation message element
        return [element.text for element in validation_message_elements]

    def get_email_validation_message(self):
        try:
            validation_message_element = self.driver.find_element(By.XPATH,
                                                                  "//p[normalize-space()='Enter a valid email']")
            return validation_message_element.text
        except NoSuchElementException:
            print("Email validation message not found.")
            return ""

    def get_password_validation_message(self):
        password_element = self.wait_for_element_visible(By.ID, "pass")
        if password_element:
            validation_message_element = password_element.find_element(By.XPATH,
                                                                       "//p[contains(text(),'Length must be minimum 8 and combination of uppercase')]")

            return validation_message_element.text if validation_message_element else ""
        return ""

    def get_password_mismatch_message(self):
        confirm_password_element = self.wait_for_element_visible(By.ID, "cpass")
        if confirm_password_element:
            validation_message_element = confirm_password_element.find_element(By.XPATH,
                                                                               "//p[normalize-space()='Password did not match']")

            return validation_message_element.text if validation_message_element else ""
        return ""

    def get_selected_gender(self):
        gender_dropdown = Select(self.wait_for_element_visible(By.ID, "gender"))
        return gender_dropdown.first_selected_option.text if gender_dropdown else ""

    def get_email_exists_message(self):
        try:
            validation_message_element = self.driver.find_element(By.XPATH,
                                                                  "//div[@id='toast-container']")
            return validation_message_element.text
        except NoSuchElementException:
            print("Email already exists validation message not found.")
            return ""

    def navigate_to_signup_page(self):
        self.driver.get("https://appradiofm.com/signup")

    def enter_otp(self, otp):
        otp_fields = self.driver.find_elements(By.XPATH, "//div//input[@type='number']")  # Adjust selector as necessary
        for i, digit in enumerate(otp):
            otp_fields[i].send_keys(digit)

    def submit_otp(self):
        verify_button = self.wait_for_element_clickable(By.XPATH, "//input[@value='VERIFY']")
        if verify_button:
            verify_button.click()
