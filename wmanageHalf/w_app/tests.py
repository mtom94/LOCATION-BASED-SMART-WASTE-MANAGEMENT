from django.test import TestCase

# Create your tests here.
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By

# Start a Selenium session
driver = webdriver.Chrome()

# Open the login page
driver.get("http://127.0.0.1:8000/show_home_admin/")

# Find email and password fields and submit button
email_field = driver.find_element(By.ID, "email")
password_field = driver.find_element(By.ID, "password")
submit_button = driver.find_element(By.ID, "submit-btn")

# Fill in email and password
email_field.send_keys("admin@gmail.com")
password_field.send_keys("admin12@A")

# Click the submit button
submit_button.click()

# Wait for a while to see the result
driver.implicitly_wait(5)

# Close the browser
driver.quit()
