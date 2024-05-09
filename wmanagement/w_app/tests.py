#-------------------------------------------Test1 Login------------------------------------------------------#


# import unittest
# from selenium import webdriver
# from selenium.webdriver.common.by import By
# from selenium.webdriver.support.ui import WebDriverWait
# from selenium.webdriver.support import expected_conditions as EC

# class LoginTest(unittest.TestCase):

#     def setUp(self):
#         self.driver = webdriver.Chrome()
#         self.driver.get("http://127.0.0.1:8000/")
#         self.driver.maximize_window()

#     def tearDown(self):
#         self.driver.quit()

#     def test_login_successful(self):
#         wait = WebDriverWait(self.driver, 10)

#         # Input email and password
#         email_input = wait.until(EC.presence_of_element_located((By.ID, "email")))
#         password_input = self.driver.find_element(By.ID, "password")
#         email_input.send_keys("admin@gmail.com")
#         password_input.send_keys("admin12@A")

#         # Wait for the submit button to become enabled
#         submit_button = wait.until(EC.element_to_be_clickable((By.ID, "submit-btn")))

#         # Click login button
#         submit_button.click()

#         # Handle alert and wait for redirection
#         wait.until(EC.alert_is_present())
#         alert = self.driver.switch_to.alert
#         self.assertEqual(alert.text, "Login Successful")
#         alert.accept()

#         redirected_url = "http://127.0.0.1:8000/show_home_admin/"
#         wait.until(EC.url_to_be(redirected_url))
#         self.assertEqual(self.driver.current_url, redirected_url)

# if __name__ == "__main__":
#     unittest.main()
#---------------------------------Test2 Update #-------------------------------------------------------------------

#