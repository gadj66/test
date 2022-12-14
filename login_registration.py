import time
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium import webdriver
driver = webdriver.Chrome(executable_path='C:/chromedriver.exe')
driver.get("http://practice.automationtesting.in/")
driver.implicitly_wait(5)
myaccount = driver.find_element_by_link_text("My Account").click()
email = driver.find_element_by_css_selector("input[type='email']")
email.send_keys("malcovich@gmail.com")
password = driver.find_element_by_id("reg_password")
password.send_keys("UTGperm59!")
#time.sleep(10)
register_btn = driver.find_element_by_css_selector("input[name='register']")
register_btn.click()