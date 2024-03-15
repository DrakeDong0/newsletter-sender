from selenium import webdriver
from selenium.webdriver import ActionChains
from selenium.webdriver.edge.service import Service
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.edge.options import Options
from selenium.webdriver.common.by import By
import time
import sys
import os

email = sys.argv[1]

count = 0

driver_path = "C:/Users/drake/Desktop/Projects\spam_em/edgedriver_win64/msedgedriver.exe"
service = Service(executable_path=driver_path)

options = Options()
options.add_argument("--headless")
options.add_argument("--disable-gpu") 

driver = webdriver.Edge(service=service, options=options)

#Functions
def set_viewport_size(driver, width, height):
    window_size = driver.execute_script("""
        return [window.outerWidth - window.innerWidth + arguments[0],
          window.outerHeight - window.innerHeight + arguments[1]];
        """, width, height)
    driver.set_window_size(*window_size)
set_viewport_size(driver, 1500, 1000)

def wait(seconds):
    time.sleep(seconds)


#Website interaction
driver.get('https://www.helpscout.com/blog/')
checkbox1 = driver.find_element(By.NAME, "legal--17378213")
checkbox2 = driver.find_element(By.NAME, "legal--1261029")
checkbox1.click()
checkbox2.click()
email_input = driver.find_element(By.ID, "bb44a54a-5eb9-49aa-adbc-cc247f4fbfa1-email")
email_input.send_keys(email)
subscribe = driver.find_element(By.CLASS_NAME, "submit-button")
subscribe.click()
count += 1

driver.get('https://www.atlasobscura.com/newsletters')
button = driver.find_element(By.CSS_SELECTOR, 'button.aon-primary-button.inline-block[data-action="click->checkboxes#selectAll"]')
driver.execute_script("window.scrollBy(0, 100);")
button.click()
email_input = driver.find_element(By.ID, 'email-newsletters')
email_input.send_keys(email)
submit_button = driver.find_element(By.NAME, 'commit')
submit_button.click()
count += 1

os.system('cls')
print("Signed up for ", count, " newsletters :)")


driver.quit()
