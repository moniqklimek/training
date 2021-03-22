import json
import pprint

"""
TITLE: imagine buy in bookshoop - interaktive fun with User :) 

ISSUE : help you choose the right item, get to know the User's preferences, i.e. - the thematic category that interests him, the results improved for him, a detailed description of the selected item

assumptions:
no method has been developed to protect the program against entering incorrect answers by the User
established:
- that the categories will be written as displayed on the console with uppercase letters (no spaces, etc.)
- that the user will copy the entire title of the book as it is displayed on the console

logic
100. Ask the user what category of prince interests him(show him the sorted results)

101. Enter the selected category and ask if User wants to sort them by:
        - increasing price,
        - decreasing price,
        - the highest number of stars,
        - the lowest number of stars,
        - availability,
and present the results

102.The user has chosen a given book - show him a short description and product description


logika - PL
100. spytaj Kupujacego jaka kategoria ksiazego go intresuje (pokaz mu posortowane wyniki)

101. wejdz do wybranej kategori i spytaj czy Kupujacy chce posortowac je po:
- cenie rosnacej,
- cenie malejacej,
- najwyzszej ilosci gwiazdek,
- najnizszej ilosci gwiazdek,
- dostepnosci,
i zaprezentuj wyniki do dalszego wyboru w postaci listy

102. user wybral dana ksiazke - pokaz mu do niej szczegolowy opis i opis produktu 
"""

# open and read the content of files from part 01 this issue (scraping results)
f1 = open('resources/01_category_first_link.json')
scrap1 = json.load(f1)
f1.close()

f2 = open('resources/02_single_books.json')
scrap2 = json.load(f2)
f2.close()

f3 = open('resources/03_details_single_books.json')
scrap3 = json.load(f3)
f3.close()


class Game:
    def __init__(self):
        pass
    
    # I am using a file called --> "01_category_first_link.json"
    # important because each file has different keys to access the content of the dictionaries
    def sorted_thematica_category(self,s1):
        category_list = [letter['Book_Category'] for letter in s1]
        sorted_category_list = sorted(category_list)
        return sorted_category_list
    
    # I am using a file called --> "02_single_books.json"
    def show_all_books_ctagory(self, s2, choosen_category):
        list_all_books_this_cat=[]
        for el in s2:
            if el['Book_Category'] == choosen_category:
                list_all_books_this_cat.append(el['Book_Title'])
        how_many_books = len(list_all_books_this_cat)
        return how_many_books, list_all_books_this_cat
    
    def printing_long_questions(self):
            print('--------')
            print('Please tell me how to sort the results for YOU. Write 1 or 2 or 3 or 4 or 5.')
            print(' \t\t  1 - sort by price - DESC.')
            print(' \t\t  2 - sort by price - ASC.')
            print(' \t\t  3 - sort by popularity ranking - DESC.')
            print(' \t\t  4 - sort by popularity ranking - ASC.')
            print(' \t\t  5 - sort by Title alphabetically. ')


    def user_choose_filter_method(self, nr, list_title):
        if nr==1 or nr==2:
            list_dict_title_and_price=self.generate_tab_title_price(scrap2, list_title)
            if nr == 1:
                result_method = self.sort_method_1(list_dict_title_and_price)
            else:
                #nr 2
                result_method = self.sort_method_2(list_dict_title_and_price)

        if nr == 3:
            # create dict only with key like stars and title
            list_dict_title_and_stars = self.generate_tab_title_stars(scrap2, list_title)
            # sorted by stars 
            result_method = self.sort_method_3(list_dict_title_and_stars)

        if nr == 4:
            # create dict only with key like stars and title
            list_dict_title_and_stars = self.generate_tab_title_stars(scrap2, list_title)
            # sorted by stars
            result_method = self.sort_method_4(list_dict_title_and_stars)

        if nr == 5:
            result_method = self.sort_method_5(list_title)
        return result_method 


    #           building a new DICTIONARY  - cutting the content from existing DICTIONARIES
    # idea from https://stackoverflow.com/questions/3420122/filter-dict-to-contain-only-certain-keys
    def remove_key_from_existing_dict(self, existing_dict, *key_to_delete_from_existing_dict):
        """
        input -{'Book_Price': 10.97, 'Book_Stars': 1, 'Book_Title': 'The Long Shadow', 'Book_total_category_amouth': 1}
        key_to_delete_from_existing_dict='Book_Stars'

        output--> {'Book_Price': 10.97,'Book_Title': 'The Long Shadow', , 'Book_total_category_amouth': 1}
        """
        new_dict = dict((key, value) for key, value in existing_dict.items() if key not in key_to_delete_from_existing_dict)
        return new_dict
    

    def leave_only_selected_keys_in_existing_dict(self,existing_dict, *key_to_stay):
        """
        input -{'Book_Price': 10.97, 'Book_Stars': 1, 'Book_Title': 'The Long Shadow', 'Book_total_category_amouth': 1}
        key_to_stay='Book_Stars', 'Book_Title'

        output--> {'Book_Stars': 1, 'Book_Title': 'The Long Shadow'}
        """
        new_dict = dict((key, value) for key, value in existing_dict.items() if key in key_to_stay)
        return new_dict



    #           building a new list of dictionaries - cutting the content from skraping 2 (list - dictionaries)

    def generate_tab_title_price(self, scrap2, list_title):
        # scrap2= big list dics
        # i want filter and catch only interesting me title --list_title
        # and return only key --'Book_Price', 'Book_Title'
        list_dict_only_title_price=[]
        for small_dict in scrap2:
            for title in list_title:
                if small_dict['Book_Title'] in title:
                    new_short_dict = self.leave_only_selected_keys_in_existing_dict(small_dict, 'Book_Price', 'Book_Title')
                    list_dict_only_title_price.append(new_short_dict)

        return list_dict_only_title_price
       
    def generate_tab_title_stars(self, scrap2, list_title):
            # scrap2= big list dics
            # i want filter and catch only interesting me title --list_title
        # and return only key --'Book_Title', 'Book_Stars'
        list_dict_only_title_stars = []
        for small_dict in scrap2:
            for title in list_title:
                if small_dict['Book_Title'] in title:
                    new_short_dict = self.leave_only_selected_keys_in_existing_dict(
                        small_dict, 'Book_Title', 'Book_Stars')
                    list_dict_only_title_stars.append(new_short_dict)

        return list_dict_only_title_stars
        


    def sort_method_1(self,list_dict_title_and_price):
        #Press 1 - sort by price descending (malejaco) 
        # return list with dict price and title
        # inspiration - -> https: // stackoverflow.com/questions/1143671/how-to-sort-objects-by-multiple-keys-in-python
        sorted_by_price_DESC= sorted(list_dict_title_and_price, key=lambda d: (-d['Book_Price'], d['Book_Title']))
        return sorted_by_price_DESC
        
    def sort_method_2(self, list_dict_title_and_price):
        #  Press 2 - sorted by price in ascending order (rosnaco)
        # return list with dict price and title
        sorted_by_price_DESC = sorted(list_dict_title_and_price, key=lambda d: (-d['Book_Price'], d['Book_Title']))
        sorted_by_price_ASC = sorted_by_price_DESC[::-1]
        return sorted_by_price_ASC
               
    def sort_method_3(self, list_dict_only_title_AND_stars):
        sorted_by_stars_DESC = sorted(list_dict_only_title_AND_stars, key=lambda d: (-d['Book_Stars'], d['Book_Title']))
        return sorted_by_stars_DESC

    def sort_method_4(self, list_dict_only_title_AND_stars):
        # catch list dict with stars and title and return sorted by stars 
        #Press 3 - sorted by popularity ranking - Max stars to min
        sorted_by_stars_DESC = sorted(list_dict_only_title_AND_stars, key=lambda d: (-d['Book_Stars'], d['Book_Title']))
        sorted_by_stars_ASC = sorted_by_stars_DESC[::-1]
        return sorted_by_stars_ASC
       
    def sort_method_5(self, list_title):
     
        # Press 5 - sort by title alphabetically
        """
        ["It's Only the Himalayas", 'Full Moon over Noah’s Ark: An Odyssey to Mount Ararat and Beyond', 'See America: A Celebration of Our National Parks & Treasured Sites', 'Vagabonding: An Uncommon Guide to the Art of Long-Term World Travel', 'Under the Tuscan Sun',
            'A Summer In Europe', 'The Great Railway Bazaar', 'A Year in Provence (Provence #1)', 'The Road to Little Dribbling: Adventures of an American in Britain (Notes From a Small Island #2)', 'Neither Here nor There: Travels in Europe', '1,000 Places to See Before You Die']
        """
        # mamy kategorie wybrana, mamy liste ksiazek - sort by price descending.
        sorted_title = sorted(list_title)
        return sorted_title



   
   
    # choose inf detail from scrap 3 
    # I am using a file called --> "03_details_single_books.json"
    def catch_index_if_have_title(self,title_choosen, scrap3):
        # output: list dicts
        # purpose: catch only index - for concret - value :title_choosen
        # which help to link another parts this dict with information like

        counter_index_in_list_dicts = 0
        for el in scrap3:
            if el['title_book'] == title_choosen:
                break
            else:
                counter_index_in_list_dicts += 1
        return counter_index_in_list_dicts

    def return_details(self,title_choosen, scrap3):
        # i need index link with this title 
        index_list_with_dicts = self.catch_index_if_have_title(title_choosen, scrap3)

        tab_details=[]

        title_book = scrap3[index_list_with_dicts]["title_book"]
        tab_details.append(title_book)

        category = scrap3[index_list_with_dicts]["category"]
        tab_details.append(category)

        price = scrap3[index_list_with_dicts]["price"]
        tab_details.append(price)

        productDescription = scrap3[index_list_with_dicts]["productDescription"]
        tab_details.append(productDescription)

        how_many = scrap3[index_list_with_dicts]["in_stock_how_many_available"]
        tab_details.append(how_many)

        about = scrap3[index_list_with_dicts]['detals_link_to_book']
        tab_details.append(about)

        upc = scrap3[index_list_with_dicts]["productInformation_UPC"]
        tab_details.append(upc)
        return tab_details






    def printing_final_result(self, tab_details):
        title_book = tab_details[0]
        category = tab_details[1]
        category = tab_details[1]
        price = tab_details[2]
        productDescription = tab_details[3]
        in_stock_how_many_available = tab_details[4]
        detals_link_to_book = tab_details[5]
        productInformation_UPC = tab_details[6]
       
        print('\n\t The book has a title: {}.Category is {}'.format(title_book, category))
        print('\n\t Book Price:', price)
        print('\n\t Content Description:', productDescription)
        print('\n\t We still have {} item/s in stock'.format(in_stock_how_many_available))
        print('\n\t If you want to know more about the book, please open the link:', detals_link_to_book)
        print('\n\t UPC number:', productInformation_UPC)
       
       
     
    # logic for conversation with User through Terminal 
    def logic(self):
        answer1_user_if_play = input("Do you want to buy some interesting book? :) . Choose (n/y) \n")
        if answer1_user_if_play == 'y':
            print('--------')
            print("\t Lets game :) ..... \n\t Below thematical book's Category for Your choose. \n")
            #step one - choose category
            sorted_category = self.sorted_thematica_category(scrap1)
            print(sorted_category)

            print('--------')
            customer_choose_category_book = input(
                '\t Please choose one and copy Your choice here ...\n\t (EXAMPLE:... Academic)\n\t (EXAMPLE:... Add a comment)\n\t YOUR TURN - Chose one Category from list : ...')

            """
            while customer_choose_category_book not in sorted_category_list:
                print('Please once again choose category. This one not exist in own base and list at top')
            """
            if customer_choose_category_book in sorted_category:
                how_books, title_books_this_choosen_category = self.show_all_books_ctagory(scrap2, customer_choose_category_book)
                print('We have for You in shop {} book/books title for category {}'.format(how_books, customer_choose_category_book))
                print(title_books_this_choosen_category)
            else:
                print('Please once again choose category. This one not exist in own base and list at top')
                
            
            # step two - choose how  user want to sort results and what want to see
            self.printing_long_questions()
            nr_choosen_method=int(input())
            print(title_books_this_choosen_category)
            print('--------')
            lista_books_filter_by_user_mean=self.user_choose_filter_method(nr_choosen_method, title_books_this_choosen_category)
            

            if len(lista_books_filter_by_user_mean)==1:
                print('\t It is exactly one book in this category')
                print('--------')
                # any sens to choose book , if exist only one
                # for example for catgeory crime - [{'Book_Stars': 1, 'Book_Title': 'The Long Shadow of Small Ghosts: Murder and Memory in an American City'}]
                
                user_choose_single_title = lista_books_filter_by_user_mean[0]['Book_Title']
                tab_inf = self.return_details(user_choose_single_title, scrap3)
                #print(tab_inf)
                self.printing_final_result(tab_inf)

            else:
                print('\t Also this is list for You')
                print(lista_books_filter_by_user_mean)
                # choose single title book from User input- purpose--> show for this book all details
                user_choose_single_title = input('\t\n Now please, copy and paste the entire Title of the book here:...(EXAMPLE:... Feathers: Displays of Brilliant Plumage) ')
                # use the scrap nr 3 with details 

                tab_inf=self.return_details(user_choose_single_title,scrap3)
                print(tab_inf)
                self.printing_final_result(tab_inf)

        if answer1_user_if_play in ('n','n ','n   ', 'NO', 'nie', 'N'):
            print('Nice day any way.')
                           

if __name__ == "__main__":
    game = Game()
    game.logic()
   


