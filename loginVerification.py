import time

import self

import string
from random import random
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.support.select import Select
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.action_chains import ActionChains
from selenium.common.exceptions import NoSuchElementException

EmployeeName = "YASWANTH"
options = webdriver.ChromeOptions()
options.add_argument("--start-maximized")
driver = webdriver.Chrome("../Drivers/chromedriver.exe", 0, options)
driver.get("https://opensource-demo.orangehrmlive.com/")
wait = WebDriverWait(driver, 30)
print('--- Logging into Application ---')


def to_login(user_id, password):
    wait.until(EC.presence_of_element_located((By.NAME, "username")))
    wait.until(EC.presence_of_element_located((By.NAME, "password")))
    driver.find_element(By.XPATH, "//input[@name='username']").send_keys(user_id)
    driver.find_element(By.XPATH, "//input[@name='password']").send_keys(password)
    wait.until(EC.element_to_be_clickable((By.XPATH, "//button[@type='submit']")))
    driver.find_element(By.XPATH, "//button[@type='submit']").click()


def Add_Employee():
    wait.until(EC.presence_of_element_located((By.XPATH, "//button[text()=' Add ']")))
    driver.find_element(By.XPATH, "//button[text()=' Add ']").click()
    driver.implicitly_wait(10)
    WebDriverWait(driver, 20).until(EC.visibility_of_element_located((By.NAME, "firstName")))
    WebDriverWait(driver, 20).until(EC.presence_of_element_located((By.NAME, "firstName")))
    driver.find_element(By.NAME, "firstName").send_keys(EmployeeName)
    WebDriverWait(driver, 20).until(EC.presence_of_element_located((By.NAME, "lastName")))
    driver.find_element(By.NAME, "lastName").send_keys("BEEJA")
    driver.implicitly_wait(10)
    driver.find_element(By.XPATH, "//button[@type='submit']").click()
    driver.implicitly_wait(2)
    WebDriverWait(driver, 20).until(
        EC.visibility_of_element_located((By.XPATH, "//p[text()='Successfully Saved']")))
    time.sleep(2)
    WebDriverWait(driver, 50).until(EC.presence_of_element_located(
        (By.XPATH, "//label[contains(text(),'Other Id')]/parent::div/following-sibling::div//input")))
    WebDriverWait(driver, 50).until(EC.element_to_be_clickable(
        (By.XPATH, "//label[contains(text(),'Other Id')]/parent::div/following-sibling::div//input")))
    driver.find_element(By.XPATH,
                             "//label[contains(text(),'Other Id')]/parent::div/following-sibling::div//input").send_keys(
        "64538")
    driver.implicitly_wait(2)
    time.sleep(2)
    WebDriverWait(driver, 20).until(EC.presence_of_element_located(
        (By.XPATH, "//label[contains(text(),'Driver')]/parent::div/following-sibling::div//input")))
    WebDriverWait(driver, 20).until(EC.element_to_be_clickable(
        (By.XPATH, "//label[contains(text(),'Driver')]/parent::div/following-sibling::div//input")))
    driver.find_element(By.XPATH,
                             "//label[contains(text(),'Driver')]/parent::div/following-sibling::div//input").send_keys(
        "23478")
    driver.implicitly_wait(2)
    time.sleep(2)
    WebDriverWait(driver, 20).until(EC.presence_of_element_located(
        (By.XPATH, "//label[contains(text(),'SSN Number')]/parent::div/following-sibling::div//input")))
    WebDriverWait(driver, 20).until(EC.element_to_be_clickable(
        (By.XPATH, "//label[contains(text(),'SSN Number')]/parent::div/following-sibling::div//input")))
    driver.find_element(By.XPATH,
                             "//label[contains(text(),'SSN Number')]/parent::div/following-sibling::div//input").send_keys("234787654")
    driver.implicitly_wait(2)
    time.sleep(2)
    WebDriverWait(driver, 20).until(EC.presence_of_element_located(
        (By.XPATH, "//label[contains(text(),'SIN Number')]/parent::div/following-sibling::div//input")))
    WebDriverWait(driver, 20).until(EC.element_to_be_clickable(
        (By.XPATH, "//label[contains(text(),'SIN Number')]/parent::div/following-sibling::div//input")))
    driver.find_element(By.XPATH,
                             "//label[contains(text(),'SIN Number')]/parent::div/following-sibling::div//input").send_keys(
        "787654")
    driver.implicitly_wait(5)
    time.sleep(2)
    driver.find_element(By.XPATH,
                             "//label[contains(text(),'Gender')]/parent::div/following-sibling::div//label[text()='Female']").click()
    driver.find_element(By.XPATH, "//label[contains(text(),'Nationality')]/parent::div/following-sibling::div//div[text()='-- Select --']").click()
    time.sleep(2)
    WebDriverWait(driver, 20).until(
        EC.presence_of_element_located((By.XPATH, "//div[@role='option']/span[text()='Indian']")))
    driver.find_element(By.XPATH, "//div[@role='option']/span[text()='Indian']").click()
    time.sleep(2)
    driver.find_element(By.XPATH, "//label[contains(text(),'Marital Status')]/parent::div/following-sibling::div//div[text()='-- Select --']").click()
    WebDriverWait(driver, 20).until(
        EC.presence_of_element_located((By.XPATH, "//div[@role='option']/span[text()='Single']")))
    driver.find_element(By.XPATH, "//div[@role='option']/span[text()='Single']").click()
    driver.implicitly_wait(2)
    time.sleep(2)
    WebDriverWait(driver, 20).until(EC.presence_of_element_located(
        (By.XPATH, "//label[contains(text(),'License Expiry Date')]/parent::div/following-sibling::div//input")))
    WebDriverWait(driver, 20).until(EC.element_to_be_clickable(
        (By.XPATH, "//label[contains(text(),'License Expiry Date')]/parent::div/following-sibling::div//input")))
    driver.find_element(By.XPATH,
                             "//label[contains(text(),'License Expiry Date')]/parent::div/following-sibling::div//input").click()
    WebDriverWait(driver, 20).until(
        EC.presence_of_element_located((By.XPATH, "//div[@class='oxd-calendar-date --today']")))
    driver.find_element(By.XPATH, "//div[@class='oxd-calendar-date --today']").click()
    WebDriverWait(driver, 20).until(EC.presence_of_element_located(
        (By.XPATH, "//label[contains(text(),'Date of Birth')]/parent::div/following-sibling::div//input")))
    WebDriverWait(driver, 20).until(EC.element_to_be_clickable(
        (By.XPATH, "//label[contains(text(),'Date of Birth')]/parent::div/following-sibling::div//input")))
    time.sleep(2)
    driver.find_element(By.XPATH,
                             "//label[contains(text(),'Date of Birth')]/parent::div/following-sibling::div//input").click()
    WebDriverWait(driver, 20).until(
        EC.presence_of_element_located((By.XPATH, "//div[@class='oxd-calendar-date --today']")))
    driver.find_element(By.XPATH, "//div[@class='oxd-calendar-date --today']").click()
    driver.implicitly_wait(2)
    driver.find_element(By.XPATH, "//button[@type='submit']").click()
    driver.implicitly_wait(2)
    WebDriverWait(driver, 20).until(
        EC.visibility_of_element_located((By.XPATH, "//p[text()='Successfully Updated']")))
    time.sleep(2)



def Click_PIM():
    wait.until(EC.presence_of_element_located((By.XPATH, "//span[text()='PIM']")))
    driver.find_element(By.XPATH, "//span[text()='PIM']").click()
    driver.implicitly_wait(10)




def Click_Edit():
    wait.until(EC.presence_of_element_located((By.XPATH, "(//div[text()='BEEJA']//parent::div/following-sibling::div[5]//div//button[2])[1]")))
    driver.find_element(By.XPATH, "(//div[text()='BEEJA']//parent::div/following-sibling::div[5]//div//button[2])[1]").click()
    driver.implicitly_wait(10)

def Click_Delete():
    wait.until(EC.presence_of_element_located((By.XPATH, "(//div[text()='BEEJA']//parent::div/following-sibling::div[5]//div//button[1])[1]")))
    driver.find_element(By.XPATH, "(//div[text()='BEEJA']//parent::div/following-sibling::div[5]//div//button[1])[1]").click()
    driver.implicitly_wait(10)
    wait.until(EC.presence_of_element_located((By.XPATH, "//button[text()=' Yes, Delete ']")))
    driver.find_element(By.XPATH,"//button[text()=' Yes, Delete ']").click()
    driver.implicitly_wait(10)
    driver.implicitly_wait(2)
    WebDriverWait(driver, 20).until(
        EC.visibility_of_element_located((By.XPATH, "//p[text()='Successfully Deleted']")))
    time.sleep(2)





def to_logout():
    driver.find_element(By.XPATH, "//span[@class='oxd-userdropdown-tab']").click()
    wait.until(EC.visibility_of_element_located((By.LINK_TEXT, 'Logout')))
    driver.find_element(By.LINK_TEXT, "Logout").click()
    wait.until(EC.presence_of_element_located((By.NAME, "username")))
    wait.until(EC.presence_of_element_located((By.NAME, "password")))
    assert "OrangeHRM" in driver.title
    print('--- Logout Successful ---')


print("-- Login via admin credentials --")
to_login(user_id="Admin6", password="admin1234")
to_login(user_id="Admin", password="admin123")
try:
    wait.until(EC.presence_of_element_located((By.LINK_TEXT, "PIM")))
    print('--- Login Successful ---\n')
    Click_PIM()
    Add_Employee()
    Click_PIM()
    Click_Edit()
    Click_PIM()
    Click_Delete()
    to_logout()
    # Add_NewUser("Yaswanth")
    # to_logout()
except NoSuchElementException:
    print(Exception)

print("-- Login via Admin User--")
driver.close()
