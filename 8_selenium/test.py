from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
import time
from selenium.webdriver.support.select import Select
import pytest


def init_website():
    driver = webdriver.Firefox()
    driver.get("https://www.saucedemo.com")
    return driver


def login(driver):
    element = driver.find_element(By.NAME, 'user-name')
    element.send_keys("standard_user")
    time.sleep(0.4)
    element = driver.find_element(By.NAME, 'password')
    element.send_keys("secret_sauce")
    time.sleep(0.4)
    driver.find_element(By.NAME, 'login-button').click()
    time.sleep(0.4)


def test_login():
    driver = init_website()
    login(driver)
    assert "https://www.saucedemo.com/inventory.html" in driver.current_url
    driver.quit()

def test_logout():
    driver = init_website()
    login(driver)
    driver.find_element(By.ID, 'react-burger-menu-btn').click()
    time.sleep(0.4)
    driver.find_element(By.ID, 'logout_sidebar_link').click()
    assert "https://www.saucedemo.com" in driver.current_url
    driver.quit()


@pytest.mark.parametrize("item", [("add-to-cart-sauce-labs-backpack"),
                                  ("add-to-cart-sauce-labs-bike-light"),
                                  ("add-to-cart-sauce-labs-bolt-t-shirt"),
                                  ("add-to-cart-sauce-labs-fleece-jacket"),
                                  ("add-to-cart-sauce-labs-onesie"),
                                  ("add-to-cart-test.allthethings()-t-shirt-(red)"),
                                  ])
def test_shopping(item):
    driver = init_website()
    login(driver)
    driver.find_element(By.ID, item).click()
    time.sleep(0.4)
    driver.find_element(By.CLASS_NAME, 'shopping_cart_link').click()
    time.sleep(0.4)
    driver.find_element(By.ID, 'checkout').click()
    element = driver.find_element(By.ID, 'first-name')
    element.send_keys("Umalat")
    time.sleep(0.4)
    element = driver.find_element(By.ID, 'last-name')
    element.send_keys("Dukuev")
    time.sleep(0.4)
    element = driver.find_element(By.ID, 'postal-code')
    element.send_keys("123456")
    time.sleep(0.4)
    driver.find_element(By.ID, 'continue').click()
    time.sleep(0.4)
    driver.find_element(By.ID, 'finish').click()
    time.sleep(0.4)
    assert "https://www.saucedemo.com/checkout-complete.html" in driver.current_url
    driver.quit()


def test_counter():
    driver = init_website()
    login(driver)
    driver.find_element(By.ID, 'add-to-cart-sauce-labs-backpack').click()
    time.sleep(0.4)
    element = driver.find_element(By.CLASS_NAME, 'shopping_cart_badge').text
    assert int(element) == 1
    driver.quit()


def test_sort_A_to_Z():
    driver = init_website()
    login(driver)
    items = driver.find_elements(By.CLASS_NAME, 'inventory_item_name')
    print()
    list = []
    for item in items:
        list.append(item.text)
    print(list)
    sorted_list = sorted(list)
    print(sorted_list)
    for i in range(len(list)):
        assert list[i] == sorted_list[i]
    driver.quit()


def select(driver, option):
    select = driver.find_element(By.CLASS_NAME, 'product_sort_container')
    select.click()
    select_element = driver.find_element(By.CSS_SELECTOR, ".product_sort_container")
    select = Select(select_element)
    select.select_by_value(option)


def test_sort_Z_to_A():
    driver = init_website()
    login(driver)
    select(driver, "za")
    items = driver.find_elements(By.CLASS_NAME, 'inventory_item_name')
    print()
    items_list = []
    for item in items:
        items_list.append(item.text)
    print(items_list)
    sorted_list = sorted(items_list, reverse=True)
    print(sorted_list)
    for i in range(len(items_list)):
        assert items_list[i] == sorted_list[i]
    driver.quit()


def test_sort_low_to_high():
    driver = init_website()
    login(driver)
    select(driver, "lohi")
    items = driver.find_elements(By.CLASS_NAME, 'inventory_item_price')
    print()
    items_list = []
    for item in items:
        items_list.append(item.text)
    print(items_list)
    sorted_list = sorted(items_list, key=lambda x: float(x[1:]))
    print(sorted_list)
    for i in range(len(items_list)):
        assert items_list[i] == sorted_list[i]
    driver.quit()


def test_sort_high_to_low():
    driver = init_website()
    login(driver)
    select(driver, "hilo")
    items = driver.find_elements(By.CLASS_NAME, 'inventory_item_price')
    print()
    items_list = []
    for item in items:
        items_list.append(item.text)
    print(items_list)
    sorted_list = sorted(items_list, key=lambda x: float(x[1:]), reverse=True)
    print(sorted_list)
    for i in range(len(items_list)):
        assert items_list[i] == sorted_list[i]
    driver.quit()


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
    driver.quit()
