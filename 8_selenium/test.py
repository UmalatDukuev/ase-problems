from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By

# driver = webdriver.Firefox()
# driver.get("https://www.saucedemo.com")

def test_login():
    driver = webdriver.Firefox()
    driver.get("https://www.saucedemo.com")
    element = driver.find_element(By.NAME, 'user-name')
    element.send_keys("standard_user")
    element = driver.find_element(By.NAME, 'password')
    element.send_keys("secret_sauce")
    driver.find_element(By.NAME, 'login-button').click()
    assert "https://www.saucedemo.com/inventory.html" in driver.current_url