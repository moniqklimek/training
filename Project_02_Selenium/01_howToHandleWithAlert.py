#env (Python37Pytesty)
# issue : how to change/accept alert
# source
# link : https://www.selenium.dev/selenium/docs/api/py/webdriver/selenium.webdriver.common.alert.html#module-selenium.webdriver.common.alert
# link2 : https://www.geeksforgeeks.org/how-to-handle-alert-prompts-in-selenium-python/
"""
Alert Methods
The major methods during handling of alerts in Selenium include –

accept() – Accepts the alert available. OK
dismiss() – Dismisses the alert available. 
send_keys(keysToSend) – Send Keys to the Alert. - NOT POSSIBLE BY THIS CASE "User dialog does not have a text box input field."
text – Gets the text of the Alert. OK
"""

from selenium import webdriver
import time
import re # i want only digit 

# import Alert  
from selenium.webdriver.common.alert import Alert 

driver = webdriver.Chrome()
link = "https://..."
driver.get(link)

# create alert object 
alert = Alert(driver) 
# the functions checks what button number was pressed by the driver
# and compares it with the information from the window allert
def pull_text_from_alert():
    text_from_alert=alert.text
    return text_from_alert

def find_nr_button_from_prompt_allert():
    text_from_alert=pull_text_from_alert()
    nr_button_from_prompt_allert= re.findall('[0-9]+', text_from_alert) #['1']
    return int(nr_button_from_prompt_allert[0])

def check_text_from_alert_prompt_for_button1(nr_button_from_User):
    text_from_alert=pull_text_from_alert()
    nr_from_prompt_text=find_nr_button_from_prompt_allert()
    #assert <condition>,<error message>
    assert text_from_alert == "You clickedButton"+str(nr_button_from_User)+".", "a should return 'You clickedButton"+str(nr_from_prompt_text)+".'"
    return text_from_alert

def accept_alert_windows_and_sleep_3s():
    # click on alert window and accept 
    alert.accept()
    time.sleep(3)


#write a text in field 01
driver.find_element_by_xpath('//*[@id="ipt1"]').send_keys("This is my first text in field 01")
"""
alternatywna metoda
driver.find_element_by_css_selector('button[id="b1"]').click()
driver.find_element_by_css_selector('button[name="butn1"]').click()
"""
time.sleep(3)
#click on "Button 1"
driver.find_element_by_xpath('//*[@id="b1"]').click()
time.sleep(3)


# METHOD 1- how check the text from alert :)
text_for_btn1=pull_text_from_alert()
#Reading a the text of a prompt for verification:
print(text_for_btn1)  #You clickedButton1.
print(text_for_btn1=="You clickedButton1.") #True


# METHOD 2- how check the text from alert - another try:)
nr_button=1
check_text_from_alert_prompt_for_button1(nr_button)
"""
#   wrong value 
#   for example if nr_button=5 not 1

Traceback (most recent call last):
  File "/Users/monika/_MK_Selenium/04_howToHandleWithAlert.py", line 55, in <module>
    check_text_from_alert_prompt_for_button1(nr_button)
  File "/Users/monika/_MK_Selenium/04_howToHandleWithAlert.py", line 36, in check_text_from_alert_prompt_for_button1
    assert text_from_alert == "You clickedButton"+str(nr_button_from_User)+".", "a should return 'You clickedButton"+str(nr_from_prompt_text)+".'"
AssertionError: a should return 'You clickedButton1.'
"""


# click on alert window and accept 
accept_alert_windows_and_sleep_3s()


# write a text in field 02
driver.find_element_by_css_selector('input[id="ipt2"]').send_keys("This is my second text in field 02")
time.sleep(3)
#click on "Button 3"
driver.find_element_by_xpath('//*[@id="b3"]').click()
time.sleep(3)
# get alert text 
text_for_btn3=pull_text_from_alert()
print(text_for_btn3)  #You clickedButton3.
#Reading a the text of a prompt for verification:
print(text_for_btn3=="You clickedButton3.")
# click on alert window and accept 
accept_alert_windows_and_sleep_3s()
"""
infro from console
You clickedButton1.
True
You clickedButton3.
True
"""

driver.quit()
