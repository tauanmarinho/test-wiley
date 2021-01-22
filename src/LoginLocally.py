import unittest
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


class LoginLocally(unittest.TestCase):

    def setUp(self):
        self.driver = webdriver.Firefox()

    def testLogin(self):
        driver = self.driver

        driver.get("https://teamshift-qa.crossknowledge.com/")
        loginButton = driver.find_element_by_xpath("//button[@type='button' and @class='button-default button-default--transparent-primary navbar-form-recovery__submit js-login-member-button']")
        loginButton.click()

        emailInput = driver.find_element_by_id("login-form__login")
        emailInput.send_keys("tauamarinho@gmail.com")

        nextButton = driver.find_element_by_xpath("//button[@type='submit' and @class='button-default js-login-form-submit']")
        nextButton.click()

        wait = WebDriverWait(driver, 10)
        passwordInput = wait.until(EC.element_to_be_clickable((By.ID, 'login-form__password')))
        passwordInput.send_keys("WLS2020qa")

        signIn = driver.find_element_by_xpath("//button[@type='submit' and @class='button-default js-login-form-submit']")
        signIn.click()

    def tearDown(self):
        self.driver.close()


if __name__ == "__main__":
    unittest.main()
