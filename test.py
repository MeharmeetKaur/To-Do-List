from selenium import webdriver
import time
from selenium.webdriver.common.keys import Keys 

browser = webdriver.Firefox()
browser.get('http://127.0.0.1/TdoList')
print("Message : T:Do opened")

time.sleep(2)

clear = browser.find_element_by_xpath('/html/body/div/form/button')
clear.click()

for i in range(2):
	task_input = browser.find_element_by_xpath('/html/body/div/div[2]/form/input')
	if i == 1:
		task_input.send_keys("Make a Tea")
	else:
		task_input.send_keys("Wash A cup")
	print("Message : Text Typed Successfully :" + str(i))

	time.sleep(2)

	add_btn = browser.find_element_by_xpath('/html/body/div/div[2]/form/button')
	add_btn.click()
	print("Message : Task Added Successfully :"+ str(i))

time.sleep(2)

task = browser.find_element_by_xpath('/html/body/div/div[3]/div/div[1]/ol/li[1]/a')
task.click()
print("Message : Task Completed 1st")

time.sleep(2)

task = browser.find_element_by_xpath('/html/body/div/div[3]/div/div[1]/ol/li[1]/a')
task.click()
print("Message : Task Completed 2nd")

time.sleep(2)

clear = browser.find_element_by_xpath('/html/body/div/form/button')
clear.click()

print("Message : Tasks Cleared")

time.sleep(2)

task_input = browser.find_element_by_xpath('/html/body/div/div[2]/form/input')
task_input.send_keys("Don't Worry I will remain here :) ")
time.sleep(2)
add_btn = browser.find_element_by_xpath('/html/body/div/div[2]/form/button')
add_btn.click()
print("Message : Task Added Successfully")

time.sleep(2)

print("Message : Closing browser")
browser.quit()

time.sleep(2)

print("Message : Reopening browser")
browser = webdriver.Firefox()
browser.get('http://127.0.0.1/TdoList')
print("Completed")