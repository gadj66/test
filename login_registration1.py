import time
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium import webdriver
driver = webdriver.Chrome(executable_path='C:/chromedriver.exe')
driver.get("http://practice.automationtesting.in/")
driver.implicitly_wait(5)
myaccount = driver.find_element_by_link_text("My Account").click()
emaillogin = driver.find_element_by_id("username")
emaillogin.send_keys("malcovich@gmail.com")
passwordlogin = driver.find_element_by_id("password")
passwordlogin.send_keys("UTGperm59!")
#time.sleep(10)
login_btn = driver.find_element_by_css_selector("input[name='login']")
login_btn.click()