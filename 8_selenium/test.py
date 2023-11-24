from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
import time
# driver = webdriver.Firefox()
# driver.get("https://www.saucedemo.com")

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


# def test_sort_Z_to_A():
# def test_sort_low_to_high():
# def test_sort_high_to_low():


def test_locked_out():
    driver = init_website()
    element = driver.find_element(By.NAME, 'user-name')
    element.send_keys("locked_out_user")
    time.sleep(0.4)
    element = driver.find_element(By.NAME, 'password')
    element.send_keys("secret_sauce")
    time.sleep(0.4)
    driver.find_element(By.NAME, 'login-button').click()
    time.sleep(0.4)
    error_message = driver.find_element(By.CLASS_NAME, 'error-message-container')
    assert error_message.is_displayed()
