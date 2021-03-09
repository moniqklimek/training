#env (Python37Pytesty)
# issue : i have classic "dropdown" in DOM /html and I need check on webpage value
# source: https://www.selenium.dev/selenium/docs/api/py/webdriver_support/selenium.webdriver.support.select.html#module-selenium.webdriver.support.select
"""
EXAMPLE
<select name="mySelect" id="sel1">
  <option value="first">Dog</option>
  <option value="second">Cat</option>
  <option value="third">Mouse</option>
</select>
"""

import time
from selenium import webdriver
from selenium.webdriver.support.select import Select


driver = webdriver.Chrome()
link = "https://..."
driver.get(link)

#       METHOD 1 - dictionary 
all_text_available_to_choose=driver.find_element_by_xpath('//*[@id="sel1"]').text
"""
print(all_text_available_to_choose)
  Dog
  Cat
  Mouse
"""

choose_value=driver.find_element_by_xpath('//*[@id="sel1"]').get_attribute('value')
#print(choose_value)#first

available_values={"first":"Dog","second":"Cat","third":"Mouse"}
dropdown_option=available_values[choose_value]
print(dropdown_option)#Dog




#       METHOD 2 - import SELECT
# look: https://www.selenium.dev/selenium/docs/api/py/webdriver_support/selenium.webdriver.support.select.html#module-selenium.webdriver.support.select 


#       METHOD 2a - import SELECT
select_element=driver.find_element_by_xpath('//*[@id="sel1"]')
#create element class Select !!!
my_sel=Select(select_element)

#options
#Returns a list of all options belonging to this select tag
available_options=my_sel.options
"""
for el in available_options:
        print(el.text)
RESULT:
  Dog
  Cat
  Mouse
"""
answer2a=my_sel.first_selected_option.text
print(answer2a)

#       METHOD 2b - import SELECT
"""
Example from webside:
from selenium.webdriver.support.ui import Select

Select(driver.find_element(By.TAG_NAME, “select”)).select_by_index(2)
"""
answer2b=Select(driver.find_element_by_xpath('//*[@id="sel1"]')).first_selected_option.text
print(answer2b)


time.sleep(3)
driver.quit()
