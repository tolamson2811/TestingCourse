import unittest
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time


class TestAuth(unittest.TestCase):
    @classmethod
    def setUp(cls):

        webdriver_service = Service('./chromedriver.exe')

        cls.driver = webdriver.Chrome(service=webdriver_service)

    @classmethod
    def tearDown(cls):
        cls.driver.quit()

    def test_invalid_email(self):
        self.driver.get('https://magicpost.vercel.app/auth')

        loginBtn = self.driver.find_element(
            By.XPATH, '//*[@id="app"]/main/form/span/p')
        loginBtn.click()

        email = self.driver.find_element(By.ID, 'email')
        email.click()
        email.send_keys('sonson')

        password = self.driver.find_element(By.ID, 'password')
        password.click()
        password.send_keys('123456')

        confirmPassword = self.driver.find_element(By.ID, 'confirm-password')
        confirmPassword.click()
        confirmPassword.send_keys('123456')

        term = self.driver.find_element(By.ID, 'term')
        term.click()

        submit = self.driver.find_element(
            By.XPATH, '//*[@id="app"]/main/form/div/button')
        submit.click()

        validate = self.driver.find_element(
            By.XPATH, '//*[@id="app"]/main/form/div/div[1]/span')
        self.assertEqual(validate.text, 'Email không hợp lệ')

    def test_invalid_password(self):
        self.driver.get('https://magicpost.vercel.app/auth')

        loginBtn = self.driver.find_element(
            By.XPATH, '//*[@id="app"]/main/form/span/p')
        loginBtn.click()

        email = self.driver.find_element(By.ID, 'email')
        email.click()
        email.send_keys('sonson@gmail.com')

        password = self.driver.find_element(By.ID, 'password')
        password.click()
        password.send_keys('123')

        confirmPassword = self.driver.find_element(By.ID, 'confirm-password')
        confirmPassword.click()
        confirmPassword.send_keys('123')

        term = self.driver.find_element(By.ID, 'term')
        term.click()

        submit = self.driver.find_element(
            By.XPATH, '//*[@id="app"]/main/form/div/button')
        submit.click()

        validate = self.driver.find_element(
            By.XPATH, '//*[@id="app"]/main/form/div/div[2]/span')
        self.assertEqual(validate.text, 'Mật khẩu phải có ít nhất 6 ký tự')

    def test_invalid_confirm_password(self):
        self.driver.get('https://magicpost.vercel.app/auth')

        loginBtn = self.driver.find_element(
            By.XPATH, '//*[@id="app"]/main/form/span/p')
        loginBtn.click()

        email = self.driver.find_element(By.ID, 'email')
        email.click()
        email.send_keys('sonson@gmail.com')

        password = self.driver.find_element(By.ID, 'password')
        password.click()
        password.send_keys('123456')

        confirmPassword = self.driver.find_element(By.ID, 'confirm-password')
        confirmPassword.click()
        confirmPassword.send_keys('1234567')

        term = self.driver.find_element(By.ID, 'term')
        term.click()

        submit = self.driver.find_element(
            By.XPATH, '//*[@id="app"]/main/form/div/button')
        submit.click()

        validate = self.driver.find_element(
            By.XPATH, '//*[@id="app"]/main/form/div/div[3]/span')
        self.assertEqual(validate.text, 'Mật khẩu không khớp')

    def test_success(self):
        self.driver.get('https://magicpost.vercel.app/auth')

        loginBtn = self.driver.find_element(
            By.XPATH, '//*[@id="app"]/main/form/span/p')
        loginBtn.click()

        email = self.driver.find_element(By.ID, 'email')
        email.click()
        email.send_keys('sonson@gmail.com')

        password = self.driver.find_element(By.ID, 'password')
        password.click()
        password.send_keys('123456')

        confirmPassword = self.driver.find_element(By.ID, 'confirm-password')
        confirmPassword.click()
        confirmPassword.send_keys('123456')

        term = self.driver.find_element(By.ID, 'term')
        term.click()

        submit = self.driver.find_element(
            By.XPATH, '//*[@id="app"]/main/form/div/button')
        submit.click()

        wait = WebDriverWait(self.driver, 10)  # Wait up to 10 seconds
        error = wait.until(
            EC.presence_of_element_located((By.CSS_SELECTOR, 'h2')))

        self.assertEqual(error.text, 'Đăng ký thành công!')

    def test_email_already_exist(self):
        self.driver.get('https://magicpost.vercel.app/auth')

        loginBtn = self.driver.find_element(
            By.XPATH, '//*[@id="app"]/main/form/span/p')
        loginBtn.click()

        email = self.driver.find_element(By.ID, 'email')
        email.click()
        email.send_keys('test@gmail.com')

        password = self.driver.find_element(By.ID, 'password')
        password.click()
        password.send_keys('123456')

        confirmPassword = self.driver.find_element(By.ID, 'confirm-password')
        confirmPassword.click()
        confirmPassword.send_keys('123456')

        term = self.driver.find_element(By.ID, 'term')
        term.click()

        submit = self.driver.find_element(
            By.XPATH, '//*[@id="app"]/main/form/div/button')
        submit.click()

        wait = WebDriverWait(self.driver, 10)  # Wait up to 10 seconds
        error = wait.until(
            EC.presence_of_element_located((By.CSS_SELECTOR, 'h2')))

        self.assertEqual(error.text, "Đăng ký thất bại!")


if __name__ == "__main__":
    unittest.main()
