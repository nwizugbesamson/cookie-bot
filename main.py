from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
import time

# driver path as Service object
service = Service("C:/Users/SAMSON/Documents/Development/chromedriver_win32/chromedriver.exe")

#driver object
driver = webdriver.Chrome(service=service)
driver.get("https://orteil.dashnet.org/cookieclicker/")


cookie = driver.find_element(By.ID, value="bigCookie")

#cookies = driver.find_element(By.CSS_SELECTOR, value='#cookies')
upgrades = []


def click_cookie():
    now = time.time()
    while time.time() < now + 5:
        cookie.click()


start = time.time()
while time.time() < start + (60*2):
    upgrades = [upgrade for upgrade in driver.find_elements(By.CSS_SELECTOR, value=".crate.upgrade.enabled")]
    products = [product for product in driver.find_elements(By.CSS_SELECTOR, value=".product.unlocked.enabled")]
    if len(upgrades) > 0:
        upgrades[-1].click()
    elif len(products) > 0:
        to_click = driver.find_element(By.ID, value=f'product{len(products)-1}')
        to_click.click()
    #     products[-1].click()
    #     print("success")

    click_cookie()


driver.quit()
