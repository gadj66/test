#отображение страницы товара
# import time
# from selenium.webdriver.common.by import By
# from selenium.webdriver.support.ui import WebDriverWait
# from selenium.webdriver.support import expected_conditions as EC
# from selenium import webdriver
# driver = webdriver.Chrome(executable_path='C:/chromedriver.exe')
# driver.get("http://practice.automationtesting.in/")
# driver.implicitly_wait(5)
# myaccount = driver.find_element_by_link_text("My Account").click()
# emaillogin = driver.find_element_by_id("username")
# emaillogin.send_keys("malcovich@gmail.com")
# passwordlogin = driver.find_element_by_id("password")
# passwordlogin.send_keys("UTGperm59!")
# login_btn = driver.find_element_by_css_selector("input[name='login']")
# login_btn.click()
# shop = driver.find_element_by_id("menu-item-40").click()
# HTML5Forms = driver.find_element_by_css_selector("img[title='Mastering HTML5 Forms']").click()
# EC.url_to_be("https://practice.automationtesting.in/product/html5-forms/")

# количество товаров в категории
# import time
# from selenium.webdriver.common.by import By
# from selenium.webdriver.support.ui import WebDriverWait
# from selenium.webdriver.support import expected_conditions as EC
# from selenium import webdriver
# driver = webdriver.Chrome(executable_path='C:/chromedriver.exe')
# driver.get("http://practice.automationtesting.in/")
# driver.implicitly_wait(5)
# myaccount = driver.find_element_by_link_text("My Account").click()
# emaillogin = driver.find_element_by_id("username")
# emaillogin.send_keys("malcovich@gmail.com")
# passwordlogin = driver.find_element_by_id("password")
# passwordlogin.send_keys("UTGperm59!")
# login_btn = driver.find_element_by_css_selector("input[name='login']")
# login_btn.click()
# shop = driver.find_element_by_id("menu-item-40").click()
# HTMLcat = driver.find_element_by_css_selector("a[href='https://practice.automationtesting.in/product-category/html/']").click()
# element = driver.find_element_by_css_selector(".product-categories > li:nth-child(2) > .count")
# element_get_text = element.text
# assert element_get_text == "(3)"

# сортировка товаров
# import time
# from selenium.webdriver.common.by import By
# from selenium.webdriver.support.ui import WebDriverWait
# from selenium.webdriver.support import expected_conditions as EC
# from selenium.webdriver.support.select import Select
# from selenium import webdriver
# driver = webdriver.Chrome(executable_path='C:/chromedriver.exe')
# driver.get("http://practice.automationtesting.in/")
# driver.implicitly_wait(5)
# myaccount = driver.find_element_by_link_text("My Account").click()
# emaillogin = driver.find_element_by_id("username")
# emaillogin.send_keys("malcovich@gmail.com")
# passwordlogin = driver.find_element_by_id("password")
# passwordlogin.send_keys("UTGperm59!")
# login_btn = driver.find_element_by_css_selector("input[name='login']")
# login_btn.click()
# shop = driver.find_element_by_id("menu-item-40").click()
# select = Select(driver.find_element_by_css_selector(".orderby"))
# select.select_by_visible_text("Default sorting")
# select.select_by_value("price")
# select = Select(driver.find_element_by_css_selector(".orderby"))
# select.select_by_visible_text("Sort by price: low to high")

# отображение, скидка товара
# import time
# from selenium.webdriver.common.by import By
# from selenium.webdriver.support.ui import WebDriverWait
# from selenium.webdriver.support import expected_conditions as EC
# from selenium.webdriver.support.select import Select
# from selenium import webdriver
# driver = webdriver.Chrome(executable_path='C:/chromedriver.exe')
# driver.get("http://practice.automationtesting.in/")
# driver.implicitly_wait(5)
# myaccount = driver.find_element_by_link_text("My Account").click()
# emaillogin = driver.find_element_by_id("username")
# emaillogin.send_keys("malcovich@gmail.com")
# passwordlogin = driver.find_element_by_id("password")
# passwordlogin.send_keys("UTGperm59!")
# login_btn = driver.find_element_by_css_selector("input[name='login']")
# login_btn.click()
# shop = driver.find_element_by_id("menu-item-40").click()
# AndroidQSG = driver.find_element_by_css_selector("img[title='Android Quick Start Guide']").click()
# oldprice = driver.find_element_by_tag_name("del")
# oldprice_get_text = oldprice.text
# assert "600.00" in oldprice_get_text
# newprice = driver.find_element_by_css_selector("ins span[class='woocommerce-Price-amount amount']")
# newprice_get_text = newprice.text
# assert "450.00" in newprice_get_text
# AndroidQSGbook = WebDriverWait(driver, 1).until(
# EC.element_to_be_clickable((By.CLASS_NAME, "images"))).click()
# closebtn = WebDriverWait(driver, 2).until(
# EC.element_to_be_clickable((By.CLASS_NAME, "pp_close"))).click()

# проверка цены в корзине
# import time
# from selenium.webdriver.common.by import By
# from selenium.webdriver.support.ui import WebDriverWait
# from selenium.webdriver.support import expected_conditions as EC
# from selenium.webdriver.support.select import Select
# from selenium import webdriver
# driver = webdriver.Chrome(executable_path='C:/chromedriver.exe')
# driver.get("http://practice.automationtesting.in/")
# driver.implicitly_wait(5)
# shop = driver.find_element_by_id("menu-item-40").click()
# HTML5WDadd_btn = driver.find_element_by_css_selector("a[data-product_id='182']").click()
# time.sleep(3)
# shoppingcartprice = WebDriverWait(driver, 1).until(
# EC.text_to_be_present_in_element((By.CLASS_NAME, "wpmenucart-contents"), "₹180.00"))
# items_count = driver.find_elements_by_class_name("cartcontents")
# if len(items_count) == 1 :
#   print("В корзине 1 товар")
# else:
#   print("Ошибка. Количество товаров в корзине: " + str(len(items_count)))

# работа в корзине
# import time
# from selenium.webdriver.common.by import By
# from selenium.webdriver.support.ui import WebDriverWait
# from selenium.webdriver.support import expected_conditions as EC
# from selenium.webdriver.support.select import Select
# from selenium import webdriver
# driver = webdriver.Chrome(executable_path='C:/chromedriver.exe')
# driver.get("http://practice.automationtesting.in/")
# driver.implicitly_wait(5)
# shop = driver.find_element_by_id("menu-item-40").click()
# driver.execute_script("window.scrollBy(0, 300);")
# HTML5WDadd_btn = driver.find_element_by_css_selector("a[data-product_id='182']").click()
# time.sleep(2)
# Masteringjavaadd_btn = driver.find_element_by_css_selector("a[data-product_id='165']").click()
# cart_btn = driver.find_element_by_class_name("wpmenucart-icon-shopping-cart-0").click()
# time.sleep(2)
# removeproduct1_btn = driver.find_element_by_css_selector("td a[data-product_id='182']").click()
# undo_btn = driver.find_element_by_link_text("Undo?").click()
# element = driver.find_element_by_css_selector("tbody > tr:nth-child(1) > td:nth-child(5) > div > input").clear()
# countproduct1 = driver.find_element_by_css_selector("tbody > tr:nth-child(1) > td:nth-child(5) > div > input")
# countproduct1.send_keys (3)
# update_btn = driver.find_element_by_css_selector("input[value='Update Basket']").click()
# product1value = driver.find_element_by_css_selector("tbody > tr:nth-child(1) > td:nth-child(5) > div > input")
# product1value_check = product1value.get_attribute("value")
# assert product1value_check == "3"
# time.sleep(2)
# coupon_btn = driver.find_element_by_css_selector("input[value='Apply Coupon']").click()
# message = driver.find_element_by_class_name("woocommerce-error")
# message_get_text = message.text
# assert message_get_text == "Please enter a coupon code."

# покупка товара
# import time
# from selenium.webdriver.common.by import By
# from selenium.webdriver.support.ui import WebDriverWait
# from selenium.webdriver.support import expected_conditions as EC
# from selenium.webdriver.support.select import Select
# from selenium import webdriver
# driver = webdriver.Chrome(executable_path='C:/chromedriver.exe')
# driver.get("http://practice.automationtesting.in/")
# driver.implicitly_wait(5)
# shop = driver.find_element_by_id("menu-item-40").click()
# driver.execute_script("window.scrollBy(0, 300);")
# HTML5WDadd_btn = driver.find_element_by_css_selector("a[data-product_id='182']").click()
# time.sleep(2)
# cart_btn = driver.find_element_by_class_name("wpmenucart-icon-shopping-cart-0").click()
# PROCEEDTOCHECK = WebDriverWait(driver, 2).until(
# EC.element_to_be_clickable((By.CSS_SELECTOR, ".wc-proceed-to-checkout a[class='checkout-button button alt wc-forward']"))).click()
# firstname = driver.find_element_by_id("billing_first_name")
# firstname.send_keys("firstname")
# lastname = driver.find_element_by_id("billing_last_name")
# lastname.send_keys("secondname")
# email = driver.find_element_by_id("billing_email")
# email.send_keys("malcovich@gmail.com")
# phone = driver.find_element_by_id("billing_phone")
# phone.send_keys("89223333333")
