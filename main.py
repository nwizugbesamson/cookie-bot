from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.common.exceptions import NoSuchElementException
import time


service = Service("C:/Users/SAMSON/Documents/Development/chromedriver_win32/chromedriver.exe")

driver = webdriver.Chrome(service=service)
driver.get("https://orteil.dashnet.org/cookieclicker/")


cookie = driver.find_element(By.ID, value="bigCookie")

cookies = driver.find_element(By.CSS_SELECTOR, value='#cookies')
upgrades = []


def click_cookie():
    now = time.time()
    while time.time() < now + 5:
        cookie.click()


driver.maximize_window()
time.sleep(3)
driver.find_element(By.XPATH, value='/html/body/div[1]/div/a[1]').click()
start = time.time()
while time.time() < start + (60*5):
    upgrades = [upgrade for upgrade in driver.find_elements(By.CSS_SELECTOR, value=".crate.upgrade.enabled")]
    products = [product for product in driver.find_elements(By.CSS_SELECTOR, value=".product.unlocked.enabled")]
    if len(upgrades) > 0:
        upgrades[-1].click()
    elif len(products) > 0:
        products[-1].click()
        print("success")
    click_cookie()
    try:
        driver.find_element(By.XPATH, value='//*[@id="notes"]/div[3]').click()
    except NoSuchElementException:
        continue


driver.quit()
