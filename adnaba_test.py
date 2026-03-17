import time
from time import sleep
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.service import Service
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.chrome.webdriver import WebDriver
from selenium.webdriver.support.ui import Select

driver: WebDriver = webdriver.Chrome()

driver.get("https://adnabu-store-assignment1.myshopify.com/password")
driver.maximize_window()
password_field = driver.find_element(By.ID, "password")
password_field.send_keys("AdNabuQA")
password_field.send_keys(Keys.ENTER)
driver.find_element(By.CSS_SELECTOR,"summary[aria-label='Search'] span").click()
driver.find_element(By.XPATH,"//input[@id='Search-In-Modal']").send_keys("Board")
driver.find_element(By.CSS_SELECTOR,"button[aria-label='Search']").click()
driver.find_element(By.XPATH,"//a[@id='CardLink--7801364480090']").click()
driver.find_element(By.XPATH,"//button[@id='ProductSubmitButton-template--19850788667482__main']").click()
if "cart" in driver.page_source.lower() or "added" in driver.page_source.lower():
    print("Success: Product Added Successfully!")
else:
    print("Error: Product is not Added Successfully!")
