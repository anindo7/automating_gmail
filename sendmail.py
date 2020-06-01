from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import NoSuchElementException
import time

# path to your browser specific web driver
driver=webdriver.Chrome(executable_path="C:\Drivers\chromedriver_win32\chromedriver.exe")

driver.get("https://accounts.google.com/signin/v2/identifier?continue=https%3A%2F%2Fmail.google.com%2Fmail%2F&service=mail&sacu=1&rip=1&flowName=GlifWebSignIn&flowEntry=ServiceLogin")  # open url in browser

driver.maximize_window()
print(driver.title)  # get the title of the page

wait = WebDriverWait( driver, 60)  # explicit wait object
driver.find_element_by_name('identifier').send_keys("<your_email_here>"+Keys.ENTER)
ele = wait.until(EC.element_to_be_clickable((By.NAME,'password')))
ele.send_keys("<your_email_password_here>"+Keys.ENTER)

ele=wait.until(EC.title_contains('Inbox'))
try:
	driver.find_element_by_xpath("//*[@id=':l5']/div/div").click()
except NoSuchElementException:
	driver.find_element_by_xpath("//*[@id=':le']/div/div").click()


ele = wait.until(EC.element_to_be_clickable((By.NAME,'to')))
rec_email = input("Enter email of the receiver..")
ele.send_keys(rec_email)

ele=driver.find_element_by_name('subjectbox')
ele.send_keys("Test mail"+Keys.TAB+"This is a system generated mail. Please do not reply."+Keys.CONTROL+Keys.ENTER)

driver.close()