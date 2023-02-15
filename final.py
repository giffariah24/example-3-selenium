# Automation
# https://opensource-demo.orangehrmlive.com/web

import time
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.common.keys import Keys

ser_obj = Service()
driver = webdriver.Chrome(service=ser_obj)

driver.get("https://opensource-demo.orangehrmlive.com/web/")
driver.maximize_window()
time.sleep(2)

# Login
driver.find_element(By.XPATH,"//input[@placeholder='Username']").send_keys("Admin")
driver.find_element(By.XPATH,"//input[@placeholder='Password']").send_keys("admin123")
driver.find_element(By.XPATH,"//button[@type='submit']").click()

# Employee Information
name = driver.find_element(By.XPATH,"//input[@placeholder='Type for hints...']")
name.send_keys("Cecil Bonaparte")
time.sleep(2)

eid = driver.find_element(By.XPATH,"//*[@id='app']/div[1]/div[2]/div[2]/div/div[1]/div[2]/form/div[1]/div/div[2]/div/div[2]/input")
eid.send_keys("0204")
time.sleep(2)

status = driver.find_element(By.XPATH,"//*[@id='app']/div[1]/div[2]/div[2]/div/div[1]/div[2]/form/div[1]/div/div[3]/div/div[2]/div/div/div[2]/i")
status.click()
action = ActionChains(driver)
for _ in range(3):
    action.send_keys(Keys.ARROW_DOWN).perform()
    time.sleep(1)

spv = driver.find_element(By.XPATH,"//*[@id='app']/div[1]/div[2]/div[2]/div/div[1]/div[2]/form/div[1]/div/div[5]/div/div[2]/div/div/input")
spv.send_keys("Fiona Grace")
time.sleep(2)

job = driver.find_element(By.XPATH,"//*[@id='app']/div[1]/div[2]/div[2]/div/div[1]/div[2]/form/div[1]/div/div[6]/div/div[2]/div/div/div[2]")
job.click()
for _ in range(22):
    action.send_keys(Keys.ARROW_DOWN).perform()
time.sleep(2)

sub = driver.find_element(By.XPATH,"//*[@id='app']/div[1]/div[2]/div[2]/div/div[1]/div[2]/form/div[1]/div/div[7]/div/div[2]/div/div/div[2]")
sub.click()
for _ in range(4):
    action.send_keys(Keys.ARROW_DOWN).perform()
time.sleep(2)

driver.find_element(By.XPATH,"//button[@type='submit']").click()

# Edit Profile
time.sleep(3)
edit = driver.find_element(By.XPATH,"//i[@class='oxd-icon bi-pencil-fill']")
time.sleep(2)
edit.click()

time.sleep(4)
driver.back()

# Add Employee
time.sleep(2)
add = driver.find_element(By.XPATH,"//*[@id='app']/div[1]/div[2]/div[2]/div/div[2]/div[1]/button")
add.click()
time.sleep(2)

# Employee Form
driver.find_element(By.XPATH,"//input[@placeholder='First Name']").send_keys("Ujang")
driver.find_element(By.XPATH,"//input[@placeholder='Last Name']").send_keys("Buhari")
time.sleep(1)
driver.find_element(By.XPATH,"//button[@type='submit']").click()

time.sleep(5)
# Logout
profile = driver.find_element(By.XPATH,"//*[@id='app']/div[1]/div[1]/header/div[1]/div[2]/ul/li/span/i")
profile.click()
time.sleep(2)
logout = driver.find_element(By.XPATH,"//*[@id='app']/div[1]/div[1]/header/div[1]/div[2]/ul/li/ul/li[4]/a")
logout.click()

time.sleep(4)

driver.get("https://opensource-demo.orangehrmlive.com/web/leave/viewLeaveList")
driver.maximize_window()
time.sleep(2)

# Login
driver.find_element(By.XPATH,"//input[@placeholder='Username']").send_keys("Admin")
driver.find_element(By.XPATH,"//input[@placeholder='Password']").send_keys("admin123")
driver.find_element(By.XPATH,"//button[@type='submit']").click()

# Leave List
tipe = driver.find_element(By.XPATH,"//*[@id='app']/div[1]/div[2]/div[2]/div/div[1]/div[2]/form/div[1]/div/div[4]/div/div[2]/div/div/div[2]")
tipe.click()
time.sleep(1)
action = ActionChains(driver)
for _ in range(12):
    action.send_keys(Keys.ARROW_DOWN).perform()

time.sleep(2)
emp = driver.find_element(By.XPATH,"//input[@placeholder='Type for hints...']")
emp.send_keys("Ch")
time.sleep(2)
action = ActionChains(driver)
for _ in range(1):
    action.send_keys(Keys.ARROW_DOWN).perform()
    time.sleep(1)

time.sleep(3)
search = driver.find_element(By.XPATH,"//button[@type='submit']")
search.click()
search.click()

time.sleep(3)
driver.close()