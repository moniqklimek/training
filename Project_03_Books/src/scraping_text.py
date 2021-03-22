from selenium import webdriver
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
from selenium.common.exceptions import TimeoutException
import time
import json
import re
import os



class Books:
    def __init__(self):
        """ The Books class is initialized """
        pass

    #  READ INFORMATION FORM MAIN SITE - BEGIN
    #                           RESULT 01 WEBSCRAPINGU
    def catch_category_and_first_link(self):
        """
        create list dictionaries with keys: "Book_Category" and "Book_First_Link"
        and fill values from WebPage --> https://books.toscrape.com/index.html

        OUTPUT
        [{
            "Book_Category": "Travel",
            "Book_First_Link": "https://books.toscrape.com/catalogue/category/books/travel_2/index.html"
        },
        {
            "Book_Category": "Mystery",
            "Book_First_Link": "https://books.toscrape.com/catalogue/category/books/mystery_3/index.html"
        }]
        """
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
        amouth_all_books_main_page = driver.find_element_by_xpath(
            '//*[@id="default"]/div/div/div/div/form/strong[1]').text  # 1000
        return str(amouth_all_books_main_page)

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


    def catch_title_price_stars_available_link_cat(self,link):
        # single side
        # link = 'https://books.toscrape.com/catalogue/category/books/travel_2/index.html'
        # create list dicts with keys:'Book_Title','Book_Price','Book_Stars', 'Book_Available','Book_First_Link', 'Book_Category',Book_total_category_amouth'

        dict_book_title_inStock_price_stars = []

        title = driver.find_elements_by_xpath('//*[@id="default"]/div/div/div/div/section/div[2]/ol/li[//*]/article/h3/a')
        price_string = driver.find_elements_by_xpath('//*[@id="default"]/div/div/div/div/section/div[2]/ol/li[//*]/article/div[2]/p[1]')
        available = driver.find_elements_by_xpath('//*[@id="default"]/div/div/div/div/section/div[2]/ol/li[//*]/article/div[2]/p[2]')
        place_to_look_stars = driver.find_elements_by_xpath('//*[@id="default"]/div/div/div/div/section/div[2]/ol/li[//*]/article/p')  # star-rating Three

        for index in range(0, len(title)):
            # index this same
            element_title = title[index]
            element_price = price_string[index]
            element_available = available[index]
            element_star = place_to_look_stars[index]
            category = driver.find_element_by_xpath('//*[@id="default"]/div/div/div/div/div[1]/h1').text
            how_many_books = int(driver.find_element_by_xpath('//*[@id="default"]/div/div/div/div/form/strong').text)

            dict_book_title_inStock_price_stars.append(
                {
                'Book_Title': element_title.get_attribute('title'),
                'Book_Price': float((element_price.text)[1:]),
                'Book_Stars': self.change_string_rating_description_to_int((element_star.get_attribute("class")).split(" ")[-1]),
                'Book_Available': True if element_available.text == "In stock" else False,
                'Book_First_Link': link,
                'Book_Category': category,
                'Book_total_category_amouth': how_many_books}
                )

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
                results += list_books_one_category_one_page
        
            else:
                # exist more than one link for category side like :Mystery and [https://books.toscrape.com/catalogue/category/books/mystery_3/page-1.html, https://books.toscrape.com/catalogue/category/books/mystery_3/page-2.html,]
                for single_link in tab_linkow:
                    driver.get(single_link)
                    result_one_thematica_side = self.catch_title_price_stars_available_link_cat(single_link)
                    results += result_one_thematica_side
     
        return results
    #  READ INFORMATION FORM CATEGORY SITE - END

    # SAVE RESULT 01 WEBSCRAPINGU
    def save_result_from_01_web_scraping(self, tab_01):
        outputFile = "resources/01_category_first_link.json"
        with open(outputFile, 'w') as fp:
            json.dump(tab_01, fp, sort_keys=True, indent=4)

    def save_result_from_02_web_scraping(self, tab_02):
        outputFile = "resources/02_single_books.json"
        with open(outputFile, 'w') as fp:
            json.dump(tab_02, fp, sort_keys=True, indent=4)



class Single_Book:
    def __init__(self):
        """ The Single_Book class is initialized """
        pass

    def catch_info_about_book(self, link_to_book): 
        # walk into single page and create dict 
        driver.get(link_to_book)
        time.sleep(1)

        # in loop position -->for example : Alice in Wonderland (Alice's Adventures in Wonderland #1) has no descritpion !!
        try:
            description=driver.find_element_by_xpath('//*[@id="content_inner"]/article/p').text
        except:
            description='No description'

        dict_one_book_inf ={
            'detals_link_to_book': link_to_book,
            'title_book' : driver.find_element_by_xpath('//*[@id="content_inner"]/article/div[1]/div[2]/h1').text,
            'category':driver.find_element_by_xpath('//*[@id="default"]/div/div/ul/li[3]/a').text,                                       
            'in_stock_how_many_available': self.change_str_available_and_get_value_only(driver.find_element_by_xpath('//*[@id="content_inner"]/article/div[1]/div[2]/p[2]').text),
            'productDescription': description,
            'price': driver.find_element_by_xpath('//*[@id="content_inner"]/article/div[1]/div[2]/p[1]').text,
            'productInformation_UPC' : driver.find_element_by_xpath('//*[@id="content_inner"]/article/table/tbody/tr[1]/td').text
        }
        return dict_one_book_inf

    def change_str_available_and_get_value_only(self, string_description_available='In stock (19 available)'):
        #In stock (19 available) --> 19
        available_book = re.findall(r'\d+', string_description_available)
        return (int(available_book[0]))


    def catch_link_to_book(self):
        tab_single_href=[]
        single_href = driver.find_elements_by_xpath('//*[@id="default"]/div/div/div/div/section/div[2]/ol/li[//*]/article/h3/a')
        for el in single_href:
            tab_single_href.append(el.get_attribute("href"))
        return tab_single_href


    def click_link_and_look_single_book_page(self, link_single):
        # link_single - e.g. https://books.toscrape.com/catalogue/its-only-the-himalayas_981/index.html
        # methods - from the main topic page go to the book details page
        driver.get(link_single)
        time.sleep(1)
    

    def create_set_with_link_to_category_side(self,data_from_scraping2):
        """
        method leave ONLY individual links
        result
        {'https://books.toscrape.com/catalogue/category/books/travel_2/index.html',
        'https://books.toscrape.com/catalogue/category/books/mystery_3/index.html'}
        """
        set_to_category_side=set()
        for el_dict in data_from_scraping2:  # scraping2
            main_category_link=el_dict['Book_First_Link'] # mam glowny link kat-->https://books.toscrape.com/catalogue/category/books/travel_2/index.html
            set_to_category_side.add(main_category_link)
        return set_to_category_side


    def save_result_from_03_web_scraping(self, tab_03):
        outputFile = "resources/03_details_single_books.json"
        with open(outputFile, 'w') as fp:
            json.dump(tab_03, fp, sort_keys=True, indent=4)




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
    print(len(result_1)) #1000
    



    # read json file (another way to create pipline - create value and catch result scrap 2)
    f = open('resources/02_single_books.json')
    scraping2 = json.load(f)
    f.close()

    # create object class Single Book
    single_book = Single_Book()

    # generate available link to page for example -> Travel, Mystery1, Mystery2 ....
    links_to_category_pages=single_book.create_set_with_link_to_category_side(scraping2)
    # convert set --> list 
    links_to_category_pages_list = list(links_to_category_pages)

    dict_books_one_cat_detail_inf = []
    for single_link in links_to_category_pages_list:
        # single_link -->https://books.toscrape.com/catalogue/category/books/business_35/index.html
        #   open this link  
        single_book.click_link_and_look_single_book_page(single_link)
        # catch all link  from side
        hrefs_tab = single_book.catch_link_to_book()
        # created a tab of link terms go to each and download the data
        for single_link in hrefs_tab:
            # open link and fill dict for single thematical page
            details=single_book.catch_info_about_book(single_link)
            dict_books_one_cat_detail_inf.append(details)
    result_3 = dict_books_one_cat_detail_inf

    single_book.save_result_from_03_web_scraping(result_3)
    print(len(result_3))  # 1000
    
    driver.quit()
