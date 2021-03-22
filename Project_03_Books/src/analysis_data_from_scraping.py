import json
import pprint


class Date:
    def __init__(self):
        """ The Books class is initialized """
        pass

    def count_books_in_every_category(self, list_with_dict_every_books):
        dict_key_category_value_books = {}
        count = 0
        for single_book in list_with_dict_every_books:
            key = single_book['Book_Category']
            if key in dict_key_category_value_books:
                dict_key_category_value_books[key] += 1
            else:
                dict_key_category_value_books[key] = 1
        return dict_key_category_value_books

    def count_from_Book_total_category_amouth(self, list_with_dict_every_books):
        # {'Travel': 11, 'Mystery': 32}
        # 43
        dict_key_category_value_books = {}
        for el in list_with_dict_every_books:
            if el['Book_Category'] not in dict_key_category_value_books:
                dict_key_category_value_books.update({
                    el['Book_Category']: el['Book_total_category_amouth']
                })
        return dict_key_category_value_books
        #return (dict_key_category_value_books, sum(dict_key_category_value_books.values()) )
    
    # 1 scrap :)
    def check_single_side_scrap1(self, result01, hand_script_Book_Category, hand_script_Book_First_Link):
        for el in result01:
            if el['Book_Category'] == hand_script_Book_Category and el['Book_First_Link'] == hand_script_Book_First_Link:
                print("True - znaleziono w slowniku klucz {} i wartosc {} ".format(hand_script_Book_Category, hand_script_Book_First_Link))
                break
      
    def negative_check_single_side_scrap1(self, result01, hand_script_Book_Category, hand_script_Book_First_Link):
        for el in result01:
            if el['Book_Category'] == hand_script_Book_Category and el['Book_First_Link'] == hand_script_Book_First_Link:
                print(
                    "True - znaleziono w slowniku klucz {} i wartosc {} ".format(hand_script_Book_Category, hand_script_Book_First_Link))
                break
        print('FALSE -  Not found in result 01 - in list with dict key={} with values={}.'.format(hand_script_Book_Category, hand_script_Book_First_Link))
        

    def check_if_key_exist_scrap1(self, result01, hand_script_Book_Category):
        if len(list(filter(lambda x: x['Book_Category'] == hand_script_Book_Category, result01)))==1:
            print('TRUE -  found in result 01 - in list with dict key = {} .'.format(hand_script_Book_Category))
        else:
            print('FALSE - not found in result 01 - in list with dict not exist key={}.'.format(hand_script_Book_Category))










if __name__ == "__main__":
    date = Date()

    # read the date from scarping
    f1 = open('resources/01_category_first_link.json')
    f_first_scrap_category_link = json.load(f1)
    f1.close()

    f2 = open('resources/02_single_books.json')
    list_with_dict_every_books = json.load(f2)
    f2.close()

    f3 = open('resources/03_details_single_books.json')
    list_with_details = json.load(f3)
    f3.close()

    #           two independent sources and statement of results


    #           check if total amouth ==1000
    # my source file -->02_single_books.json - Key - Book_Category
    source_f2_Book_Category = date.count_books_in_every_category(list_with_dict_every_books)
    #pprint.pprint(source_f2_Book_Category)
    sum_books_source_f2_Book_Category=sum(source_f2_Book_Category.values())
    # my source file -->02_single_books.json - Key - Book_total_category_amouth

    
    dict_with_category_amouth=date.count_from_Book_total_category_amouth(list_with_dict_every_books)
    sum_books_source_f2_Book_total_category_amouth = sum(dict_with_category_amouth.values())
    print(sum_books_source_f2_Book_Category==sum_books_source_f2_Book_total_category_amouth)
    
 
 


    #           check all categories ==50
    # amouth category - date from '02_single_books.json' file
    how_many_category_02_single_books = len(source_f2_Book_Category)
    # amouth category - date from '01_category_first_link.json' file
    how_many_category_01_category_first_link=len(f_first_scrap_category_link) 
    # check if is equal 
    print(how_many_category_01_category_first_link==how_many_category_02_single_books)

    # check key and value in scraping 1 --> 01_category_first_link.json
    date.check_single_side_scrap1(f_first_scrap_category_link, "Travel", "https://books.toscrape.com/catalogue/category/books/travel_2/index.html")
    date.negative_check_single_side_scrap1(f_first_scrap_category_link, "Mystery", "https://books.toscrape.com/catalogue/category/books/travel_2/index.html")
    date.check_if_key_exist_scrap1(f_first_scrap_category_link, "Mystery")
    date.check_if_key_exist_scrap1(f_first_scrap_category_link, "MY IMAGINE NOW NEW EXTRA CATEGORY ;P ")

    # check key and value in scraping 2 --> 02_category_first_link.json =list_with_dict_every_books
    date.check_scrap2_all_field(list_with_dict_every_books, "Travel","https://books.toscrape.com/catalogue/category/books/travel_2/index.html", 45.17 ,2,"It's Only the Himalayas",11)
    date.check_scrap2_all_field(list_with_dict_every_books, ":) imagine","https://books.toscrape.com/catalogue/category/books/travel_2/index.html", 45.17, 2, "It's Only the Himalayas", 11)
