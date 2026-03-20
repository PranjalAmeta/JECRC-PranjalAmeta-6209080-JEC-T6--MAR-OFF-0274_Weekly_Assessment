from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

driver = webdriver.Chrome()
driver.maximize_window()
driver.get("https://www.google.com")
wait_obj= WebDriverWait(driver, 10)

srch= wait_obj.until(EC.visibility_of_element_located((By.NAME, "q")))
srch.send_keys("Selenium Python")


wait_obj.until(EC.visibility_of_all_elements_located((By.XPATH, "//ul[@role='listbox']//li")))
suggest = driver.find_elements(By.XPATH, "//ul[@role='listbox']//li")

for i in suggest:
    print(i.text)
suggest[1].click()

