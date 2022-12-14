from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium import webdriver
driver = webdriver.Chrome(executable_path='C:/chromedriver.exe')
driver.get("http://practice.automationtesting.in/")
driver.implicitly_wait(5)
driver.execute_script("window.scrollBy(0, 600);")
SeleniumRuby_btn = driver.find_element_by_xpath("//h3[contains(text(), 'Selenium Ruby')]")
SeleniumRuby_btn.click()
Reviews_btn = driver.find_element_by_css_selector("a[href='#tab-reviews']")
Reviews_btn.click()
starcheckbox = driver.find_element_by_css_selector("a[class='star-5']").click()
reviewtext = driver.find_element_by_tag_name("textarea")
reviewtext.send_keys("Nice book!")
name = driver.find_element_by_id("author")
name.send_keys("John")
email = driver.find_element_by_id("email")
email.send_keys("malcovich@gmail.com")
subbmit_btn = driver.find_element_by_css_selector("input[name='submit']").click()