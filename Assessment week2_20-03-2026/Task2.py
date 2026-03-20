from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.select import Select
from time import sleep

driver=webdriver.Chrome()
driver.get('https://automationexercise.com/signup')
driver.maximize_window()

wait=WebDriverWait(driver,10)
name=wait.until(EC.element_to_be_clickable((By.NAME, 'name')))
name.send_keys('kprdgdganjasafda')

email=wait.until(EC.element_to_be_clickable((By.XPATH, '//div[@class="signup-form"]/descendant::input[@name="email"]')))
email.send_keys('dhabegdsgdgp@email.com')

signup=wait.until(EC.element_to_be_clickable((By.XPATH, '//button[text()="Signup"]')))
signup.click()

mr_button=wait.until(EC.element_to_be_clickable((By.ID, 'id_gender1')))
mr_button.click()

password=wait.until(EC.element_to_be_clickable((By.ID, 'password')))
password.clear()
password.send_keys('level123')

check_field1=wait.until(EC.element_to_be_clickable((By.ID, 'newsletter')))
check_field1.click()

check_field2=wait.until(EC.element_to_be_clickable((By.ID, 'optin')))
check_field2.click()

print(check_field1.get_attribute('checked'))
print(check_field2.get_attribute('checked'))

sleep(2)
driver.quit()