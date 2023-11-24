from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
import time
from selenium.webdriver.support.select import Select

def init_website():
    driver = webdriver.Firefox()
    driver.get("https://www.saucedemo.com")
    return driver

# def test_login():
#     driver = init_website()
#     element = driver.find_element(By.NAME, 'user-name')
#     element.send_keys("standard_user")
#     time.sleep(0.4)
#     element = driver.find_element(By.NAME, 'password')
#     element.send_keys("secret_sauce")
#     time.sleep(0.4)
#     driver.find_element(By.NAME, 'login-button').click()
#     assert "https://www.saucedemo.com/inventory.html" in driver.current_url
#
# def test_logout():
#     driver = init_website()
#     element = driver.find_element(By.NAME, 'user-name')
#     element.send_keys("standard_user")
#     time.sleep(0.4)


#     element = driver.find_element(By.NAME, 'password')
#     element.send_keys("secret_sauce")
#     time.sleep(0.4)
#     driver.find_element(By.NAME, 'login-button').click()
#     time.sleep(0.4)


#     driver.find_element(By.ID, 'react-burger-menu-btn').click()
#     time.sleep(0.4)


#     driver.find_element(By.ID, 'logout_sidebar_link').click()
#     assert "https://www.saucedemo.com" in driver.current_url

# @pytest.mark.parametrize("str1, str2, expected_result", [("", "", ""),
#                                                          ("", " ", " "),
#                                                          ("123", "456!", "123456!"),
#                                                          ("abc", "def", "abcdef"),
#                                                          ("123abc", "456def", "123abc456def"),
#                                                          ("-123", "+456", "-123+456"),
#                                                          ("!123@", "_456(", "!123@_456("),
#                                                          ("-123", "+456", "-123+456"),
#                                                          ("<p>123</p>", "456", "<p>123</p>456"),
#                                                          ])
# def test_success_concat(str1, str2, expected_result):
#     assert concat(str1, str2) == expected_result


# def test_shopping():
#     driver = init_website()
#     element = driver.find_element(By.NAME, 'user-name')
#     element.send_keys("standard_user")
#     time.sleep(0.4)
#     element = driver.find_element(By.NAME, 'password')
#     element.send_keys("secret_sauce")
#     time.sleep(0.4)
#     driver.find_element(By.NAME, 'login-button').click()
#     time.sleep(0.4)
#     driver.find_element(By.ID, 'add-to-cart-sauce-labs-backpack').click()
#     time.sleep(0.4)
#     driver.find_element(By.CLASS_NAME, 'shopping_cart_link').click()
#     time.sleep(0.4)
#     driver.find_element(By.ID, 'checkout').click()
#     element = driver.find_element(By.ID, 'first-name')
#     element.send_keys("Umalat")
#     time.sleep(0.4)
#     element = driver.find_element(By.ID, 'last-name')
#     element.send_keys("Dukuev")
#     time.sleep(0.4)
#     element = driver.find_element(By.ID, 'postal-code')
#     element.send_keys("123456")
#     time.sleep(0.4)
#     driver.find_element(By.ID, 'continue').click()
#     time.sleep(0.4)
#     driver.find_element(By.ID, 'finish').click()
#     time.sleep(0.4)
#     assert "https://www.saucedemo.com/checkout-complete.html" in driver.current_url


# def test_counter():
#     driver = init_website()
#     element = driver.find_element(By.NAME, 'user-name')
#     element.send_keys("standard_user")
#     time.sleep(0.4)
#     element = driver.find_element(By.NAME, 'password')
#     element.send_keys("secret_sauce")
#     time.sleep(0.4)
#     driver.find_element(By.NAME, 'login-button').click()
#     time.sleep(0.4)
#     driver.find_element(By.ID, 'add-to-cart-sauce-labs-backpack').click()
#     time.sleep(0.4)
#     element = driver.find_element(By.CLASS_NAME, 'shopping_cart_badge').text
#     assert int(element) == 1

# def test_sort_A_to_Z():
#     driver = init_website()
#     element = driver.find_element(By.NAME, 'user-name')
#     element.send_keys("standard_user")
#     time.sleep(0.4)
#     element = driver.find_element(By.NAME, 'password')
#     element.send_keys("secret_sauce")
#     time.sleep(0.4)
#     driver.find_element(By.NAME, 'login-button').click()
#     time.sleep(0.4)
#     items = driver.find_elements(By.CLASS_NAME, 'inventory_item_name')
#     print()
#     list = []
#     for item in items:
#         list.append(item.text)
#     print(list)
#     sorted_list = sorted(list)
#     print(sorted_items)
#     for i in range(len(list)):
#         assert list[i] == sorted_list[i]


# def test_sort_Z_to_A():
#     driver = init_website()
#     element = driver.find_element(By.NAME, 'user-name')
#     element.send_keys("standard_user")
#     time.sleep(0.4)
#     element = driver.find_element(By.NAME, 'password')
#     element.send_keys("secret_sauce")
#     time.sleep(0.4)
#     driver.find_element(By.NAME, 'login-button').click()
#     time.sleep(0.4)
#     select = driver.find_element(By.CLASS_NAME, 'product_sort_container')
#     select.click()
#     select_element = driver.find_element(By.CSS_SELECTOR, ".product_sort_container")
#     select = Select(select_element)
#     select.select_by_value("za")
#     items = driver.find_elements(By.CLASS_NAME, 'inventory_item_name')
#     print()
#     list = []
#     for item in items:
#         list.append(item.text)
#     print(list)
#     sorted_list = sorted(list, reverse=True)
#     print(sorted_list)
#     for i in range(len(list)):
#         assert list[i] == sorted_list[i]

# def test_sort_low_to_high():
#     driver = init_website()
#     element = driver.find_element(By.NAME, 'user-name')
#     element.send_keys("standard_user")
#     time.sleep(0.4)
#     element = driver.find_element(By.NAME, 'password')
#     element.send_keys("secret_sauce")
#     time.sleep(0.4)
#     driver.find_element(By.NAME, 'login-button').click()
#     time.sleep(0.4)
#     select = driver.find_element(By.CLASS_NAME, 'product_sort_container')
#     select.click()
#     select_element = driver.find_element(By.CSS_SELECTOR, ".product_sort_container")
#     select = Select(select_element)
#     select.select_by_value("lohi")
#     items = driver.find_elements(By.CLASS_NAME, 'inventory_item_price')
#     print()
#     list = []
#     for item in items:
#         list.append(item.text)
#     print(list)
#     sorted_list =sorted(list, key=lambda x: float(x[1:]))
#     print(sorted_list)
#     for i in range(len(list)):
#         assert list[i] == sorted_list[i]

# def test_sort_high_to_low():
#     driver = init_website()
#     element = driver.find_element(By.NAME, 'user-name')
#     element.send_keys("standard_user")
#     time.sleep(0.4)
#     element = driver.find_element(By.NAME, 'password')
#     element.send_keys("secret_sauce")
#     time.sleep(0.4)
#     driver.find_element(By.NAME, 'login-button').click()
#     time.sleep(0.4)
#     select = driver.find_element(By.CLASS_NAME, 'product_sort_container')
#     select.click()
#     select_element = driver.find_element(By.CSS_SELECTOR, ".product_sort_container")
#     select = Select(select_element)
#     select.select_by_value("hilo")
#     items = driver.find_elements(By.CLASS_NAME, 'inventory_item_price')
#     print()
#     list = []
#     for item in items:
#         list.append(item.text)
#     print(list)
#     sorted_list =sorted(list, key=lambda x: float(x[1:]), reverse=True)
#     print(sorted_list)
#     for i in range(len(list)):
#         assert list[i] == sorted_list[i]

#
# def test_locked_out():
#     driver = init_website()
#     element = driver.find_element(By.NAME, 'user-name')
#     element.send_keys("locked_out_user")
#     time.sleep(0.4)
#     element = driver.find_element(By.NAME, 'password')
#     element.send_keys("secret_sauce")
#     time.sleep(0.4)
#     driver.find_element(By.NAME, 'login-button').click()
#     time.sleep(0.4)
#     error_message = driver.find_element(By.CLASS_NAME, 'error-message-container')
#     assert error_message.is_displayed()
