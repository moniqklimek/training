from selenium import webdriver
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
from selenium.common.exceptions import TimeoutException
import time
import json

#driver = webdriver.Chrome()
"""link = "https://books.toscrape.com/catalogue/category/books/travel_2/index.html"
driver.get(link)
time.sleep(2)"""


class Books:
    def __init__(self):
        """ The Books class is initialized """
        pass

    #  READ INFORMATION FORM MAIN SITE - BEGIN
    #                           RESULT 01 WEBSCRAPINGU
    def catch_category_and_first_link(self):
        list_main_page_Category_and_Link = []
        #category = driver.find_elements_by_xpath('//*[@id="default"]/div/div/div/aside/div[2]/ul/li/ul/li[//*]/a')
        category = driver.find_elements(By.XPATH, '//*[@id="default"]/div/div/div/aside/div[2]/ul/li/ul/li[//*]/a')
        #first_link = driver.find_elements_by_xpath('//*[@id="default"]/div/div/div/aside/div[2]/ul/li/ul/li[//*]/a')
        first_link = driver.find_elements(By.XPATH, '//*[@id="default"]/div/div/div/aside/div[2]/ul/li/ul/li[//*]/a')

        for index in range(0, len(category)):
            # index this same
            element_category = category[index]
            element_first_link = first_link[index]

            list_main_page_Category_and_Link.append(
                {
                    'Book_Category': element_category.get_attribute('text').strip(),
                    'Book_First_Link': element_first_link.get_attribute('href')
                }
            )
        return list_main_page_Category_and_Link
    
    def check_sum_category_books_equal_result_main_page(self):
        #amouth_all_books_main_page = driver.find_element_by_xpath('//*[@id="default"]/div/div/div/div/form/strong[1]').text#1000
        #return str(amouth_all_books_main_page)
        pass
        


    #  READ INFORMATION FORM CATEGORY SITE - BEGIN
    def change_string_rating_description_to_int(self, description_str):
        """
            input Three
            out 3
        """
        dict_change_string_rating_description_to_int = {
            "One": 1,
            "Two": 2,
            "Three": 3,
            "Four": 4,
            "Five": 5
        }
        return dict_change_string_rating_description_to_int[description_str]


    def not_catch_title_price_stars_available(self):
        link = 'https://books.toscrape.com/catalogue/category/books/travel_2/index.html'
        """
        change:
            start rating - "star-rating Five" -->5
            available - "In stock" --> True  
        """
        list_book_title_inStock_price_stars = []

        title = driver.find_elements_by_xpath(
            '//*[@id="default"]/div/div/div/div/section/div[2]/ol/li[//*]/article/h3/a')
        price_string = driver.find_elements_by_xpath(
            '//*[@id="default"]/div/div/div/div/section/div[2]/ol/li[//*]/article/div[2]/p[1]')
        available = driver.find_elements_by_xpath(
            '//*[@id="default"]/div/div/div/div/section/div[2]/ol/li[//*]/article/div[2]/p[2]')
        place_to_look_stars = driver.find_elements_by_xpath(
            '//*[@id="default"]/div/div/div/div/section/div[2]/ol/li[//*]/article/p')  # star-rating Three

        for index in range(0, len(title)):
            # index this same
            element_title = title[index]
            element_price = price_string[index]
            element_available = available[index]
            element_star = place_to_look_stars[index]

            list_book_title_inStock_price_stars.append(
                {
                    'Book_Title': element_title.get_attribute('title'),
                    'Book_Price': float((element_price.text)[1:]),
                    'Book_Stars': self.change_string_rating_description_to_int((element_star.get_attribute("class")).split(" ")[-1]),
                    # element_available.text
                    'Book_Available': True if element_available.text == "In stock" else False
                }
            )
        return list_book_title_inStock_price_stars

    def catch_title_price_stars_available_link_cat(self,link):
        #single side
        #link = 'https://books.toscrape.com/catalogue/category/books/travel_2/index.html'

        dict_book_title_inStock_price_stars = []
        time.sleep(2)
        title = driver.find_elements_by_xpath(
            '//*[@id="default"]/div/div/div/div/section/div[2]/ol/li[//*]/article/h3/a')
        price_string = driver.find_elements_by_xpath(
            '//*[@id="default"]/div/div/div/div/section/div[2]/ol/li[//*]/article/div[2]/p[1]')
        available = driver.find_elements_by_xpath(
            '//*[@id="default"]/div/div/div/div/section/div[2]/ol/li[//*]/article/div[2]/p[2]')
        place_to_look_stars = driver.find_elements_by_xpath(
            '//*[@id="default"]/div/div/div/div/section/div[2]/ol/li[//*]/article/p')  # star-rating Three

        for index in range(0, len(title)):
            # index this same
            element_title = title[index]
            element_price = price_string[index]
            element_available = available[index]
            element_star = place_to_look_stars[index]
            category = driver.find_element_by_xpath(
                '//*[@id="default"]/div/div/div/div/div[1]/h1').text

            #list_book_title_inStock_price_stars.append(
           
            dict_book_title_inStock_price_stars.append({
                'Book_Title': element_title.get_attribute('title'),
                'Book_Price': float((element_price.text)[1:]),
                'Book_Stars': self.change_string_rating_description_to_int((element_star.get_attribute("class")).split(" ")[-1]),
                # element_available.text
                'Book_Available': True if element_available.text == "In stock" else False,
                'Book_First_Link': link,
                'Book_Category': category

            })
        print(dict_book_title_inStock_price_stars)
        return dict_book_title_inStock_price_stars

    def create_all_links_for_single_category(self, first_link, how_many_books):
        list_links = [first_link]
        #https://books.toscrape.com/catalogue/category/books/mystery_3/index.html
        #https://books.toscrape.com/catalogue/category/books/mystery_3/page-2.html
        how_many_next_links = how_many_books//20  # 1
        how_book_left_last_page = how_many_books % 20  # 12

        dl_ending = len('index.html')
        new_link_part_one = first_link[:-dl_ending]

        for nr_page in range(2, (2+how_many_next_links)):
            new_link_part_two = 'page-'+str(nr_page)+'.html'
            link_n = new_link_part_one+new_link_part_two
            list_links.append(link_n)

        return list_links

    def catch_everything(self,first_scrap_result):
        """
        parameters: result - first scraping - list dicts with keys: Book_Category, Book_First_Link
        function check if is one page or more and 
        scrap inf like : title, link, rating, price, available - for every book 
        and every category 
        """
        list_books_one_category_many_pages = []
        results = []

        #time.sleep(1)
        for index_el_tab in range(0, len(first_scrap_result)): 
            category = first_scrap_result[index_el_tab]['Book_Category']#Travel
            link_main = first_scrap_result[index_el_tab]['Book_First_Link']#"https://books.toscrape.com/catalogue/category/books/travel_2/index.html"

            # link to first thematica page 
            driver.get(link_main)
            time.sleep(1)
            how_many_books = str(driver.find_element_by_xpath('//*[@id="default"]/div/div/div/div/form/strong').text)  # 11

            # check if exist other links
            tab_linkow = self.create_all_links_for_single_category(link_main, int(how_many_books))
            if len(tab_linkow) == 1:
                list_books_one_category_one_page = self.catch_title_price_stars_available_link_cat(link_main)
            
            else:
                # kilka linkow poza glownym
                for single_link in tab_linkow:
                    driver.get(single_link)
                    b = self.catch_title_price_stars_available_link_cat(single_link)
                    list_books_one_category_many_pages += b
            
            results = list_books_one_category_one_page + list_books_one_category_many_pages

        return results

    #  READ INFORMATION FORM CATEGORY SITE - END

    # SAVE RESULT 01 WEBSCRAPINGU
    def save_result_from_01_web_scraping(self, tab_01):
        outputFile = "01_category_first_link.json"
        with open(outputFile, 'w') as fp:
            json.dump(tab_01, fp, sort_keys=True, indent=4)

    def save_result_from_02_web_scraping(self, tab_02):
        outputFile = "02_single_books.json"
        with open(outputFile, 'w') as fp:
            json.dump(tab_02, fp, sort_keys=True, indent=4)



if __name__ == "__main__":
    # create object class Books
    books = Books()

    #open first side
    driver = webdriver.Chrome()
    link_main = "https://books.toscrape.com/index.html"
    driver.get(link_main)
    time.sleep(2)
    # catch category and link 
    first_web_scraping = books.catch_category_and_first_link()
    print(len(first_web_scraping))
    # SAVE THE FILE TO THE FOLDER
    books.save_result_from_01_web_scraping(first_web_scraping)

    result_1 = books.catch_everything(first_web_scraping)
    books.save_result_from_02_web_scraping(result_1)
    print(len(result_1)) # check the result 724 







    driver.quit()
