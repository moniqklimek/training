#env (Python37Pytesty)
"""
The Rules:

the answers to all three riddles must completely automated

Once the riddles have been solved, click the 'Check Answers' button automatically

verify that the message 'Trial Complete' has been displayed
"""


from selenium import webdriver
import time

def choose_winner():
    # function get information from html and choose the correct name, compare before two value
    # return: name person, who has more many
    winner_name=''

    first_name=driver.find_element_by_xpath('//*[@id="block-05ea3afedc551e378bdc"]/div/div[3]/span/b').text
    value_first_name=driver.find_element_by_xpath('//*[@id="block-05ea3afedc551e378bdc"]/div/div[3]/p').text

    second_name=driver.find_element_by_xpath('//*[@id="block-05ea3afedc551e378bdc"]/div/div[4]/span/b').text
    value_second_name=driver.find_element_by_xpath('//*[@id="block-05ea3afedc551e378bdc"]/div/div[4]/p').text
    if value_first_name>value_second_name:
        winner_name=first_name
    else:
        winner_name=second_name
    # choose correct answer
    return winner_name

 
driver = webdriver.Chrome()
link = "https://...."
driver.get(link)

time.sleep(2)

#       STEP ONE
# find field and write "star"
driver.find_element_by_xpath('//*[@id="r1Input"]').send_keys("star")
#  press button "Answer"
driver.find_element_by_xpath('//*[@id="r1Btn"]').click()
#find the "password" for next step
time.sleep(2)
password=driver.find_element_by_xpath('//*[@id="passwordBanner"]/h4').text


#       STEP TWO
# find field and write password
driver.find_element_by_xpath('//*[@id="r2Input"]').send_keys(str(password))
# press button "Answer"
driver.find_element_by_xpath('//*[@id="r2Butn"]').click()
time.sleep(2)
# check if answer is correct
text_after_solve_RiddleOfSecrets=driver.find_element_by_xpath('//*[@id="successBanner1"]/h4').text
print('step two ',text_after_solve_RiddleOfSecrets=="Success!" )



#       STEP THREE
winner=choose_winner()
# write correct name
driver.find_element_by_xpath('//*[@id="r3Input"]').send_keys(winner)
time.sleep(2)

#press button "answer" and proof the answer
driver.find_element_by_xpath('//*[@id="r3Butn"]').click()
text_after_solve_TheTwoMerchants=driver.find_element_by_xpath('//*[@id="successBanner2"]/h4').text
time.sleep(2)
print('step three ',text_after_solve_TheTwoMerchants=="Success!" )


#all solve - press button "Check answers"
driver.find_element_by_xpath('//*[@id="checkButn"]').click()
time.sleep(2)

# check if all answers are correct
text_after_solve_ALL=driver.find_element_by_xpath('//*[@id="trialCompleteBanner"]/h4').text
time.sleep(2)
print('step four ',text_after_solve_ALL=="Trial Complete" )
time.sleep(2)

driver.quit()
