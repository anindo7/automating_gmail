from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time

# path to your browser specific web driver
driver=webdriver.Chrome(executable_path="C:\Drivers\chromedriver_win32\chromedriver.exe")

driver.get("https://accounts.google.com/signin/v2/identifier?continue=https%3A%2F%2Fmail.google.com%2Fmail%2F&service=mail&sacu=1&rip=1&flowName=GlifWebSignIn&flowEntry=ServiceLogin")  # open url in browser
print(driver.title)  # get the title of the page

wait = WebDriverWait( driver, 60)  # explicit wait object
driver.find_element_by_name('identifier').send_keys("<your_email_here>"+Keys.ENTER)
ele = wait.until(EC.element_to_be_clickable((By.NAME,'password')))
ele.send_keys("<your_email_password_here>"+Keys.ENTER)

ele=wait.until(EC.title_contains('Inbox'))
# mails=driver.find_elements_by_class_name('zF')
# print(len(mails))
# for m in mails[:10]:
#     print(m.get_attribute("name"))


mails=driver.find_elements_by_class_name('zE')
print(len(mails))
for m in mails:
	m.click()
	ele = wait.until(EC.element_to_be_clickable((By.XPATH,"//*[@id=':4']/div[2]/div[1]/div/div[1]/div")))
	ele.click()

driver.close()