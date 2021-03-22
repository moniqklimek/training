from game import Game
import unittest


class GameTest(unittest.TestCase):
    def setUp(self):
        self.game = Game()

    def test_sorted_thematica_category(self):
        s1 = [{
            "Book_Category": "Sports and Games",
            "Book_First_Link": "https://books.toscrape.com/catalogue/category/books/sports-and-games_17/index.html"
        },
        {
            "Book_Category": "Add a comment",
            "Book_First_Link": "https://books.toscrape.com/catalogue/category/books/add-a-comment_18/index.html"
        },
        {
            "Book_Category": "Fantasy",
            "Book_First_Link": "https://books.toscrape.com/catalogue/category/books/fantasy_19/index.html"
        }]
        data_s1 = self.game.sorted_thematica_category(s1)
        self.assertEqual(data_s1, ['Add a comment', 'Fantasy', 'Sports and Games'])
        self.assertNotEqual(data_s1, ['Fantasy', 'Sports and Games'])

    def test_show_all_books_ctagory(self):
        s2 = [
            {
                "Book_Available": True,
                "Book_Category": "Travel",
                "Book_First_Link": "https://books.toscrape.com/catalogue/category/books/travel_2/index.html",
                "Book_Price": 45.17,
                "Book_Stars": 2,
                "Book_Title": "It's Only the Himalayas",
                "Book_total_category_amouth": 11
            },
            {
                "Book_Available": True,
                "Book_Category": "Travel",
                "Book_First_Link": "https://books.toscrape.com/catalogue/category/books/travel_2/index.html",
                "Book_Price": 49.43,
                "Book_Stars": 4,
                "Book_Title": "Full Moon over Noah’s Ark: An Odyssey to Mount Ararat and Beyond",
                "Book_total_category_amouth": 11
            
            }]
        data_s2=self.game.show_all_books_ctagory(s2,'Travel')
        self.assertEqual(data_s2, (2, ["It's Only the Himalayas", "Full Moon over Noah’s Ark: An Odyssey to Mount Ararat and Beyond"]))

        s2_a = [{
            "Book_Available": True,
            "Book_Category": "Travel",
            "Book_First_Link": "https://books.toscrape.com/catalogue/category/books/travel_2/index.html",
            "Book_Price": 26.08,
            "Book_Stars": 5,
            "Book_Title": "1,000 Places to See Before You Die",
            "Book_total_category_amouth": 11
        },
            {
            "Book_Available": True,
            "Book_Category": "Mystery",
            "Book_First_Link": "https://books.toscrape.com/catalogue/category/books/mystery_3/index.html",
            "Book_Price": 47.82,
            "Book_Stars": 4,
            "Book_Title": "Sharp Objects",
            "Book_total_category_amouth": 32
        }]
        data_s2_a = self.game.show_all_books_ctagory(s2_a, 'Travel')
        self.assertEqual(data_s2_a, (1, ["1,000 Places to See Before You Die"]))

        data_s2_b = self.game.show_all_books_ctagory(s2_a, 'Mystery')
        self.assertEqual(data_s2_b, (1, ["Sharp Objects"]))

    def test_remove_key_from_existing_dict(self):
        existing_dict = {
            "Book_Price": 10.97, 
            "Book_Stars": 1, 
            "Book_Title": 'The Long Shadow', 
            "Book_total_category_amouth": 1
            }
        key_title_to_delete_from_existing_dict = "Book_Title"
        result=self.game.remove_key_from_existing_dict(existing_dict,key_title_to_delete_from_existing_dict)
        self.assertEqual(result, {"Book_Price": 10.97,
                                  "Book_Stars": 1,
                                  "Book_total_category_amouth": 1})

        key_price_to_delete_from_existing_dict = "Book_Price"
        result = self.game.remove_key_from_existing_dict(existing_dict, key_price_to_delete_from_existing_dict)
        self.assertEqual(result, {"Book_Stars": 1,
                                  "Book_Title": 'The Long Shadow',
                                  "Book_total_category_amouth": 1
                                  })

       


    def test_leave_only_selected_keys_in_existing_dict(self):
        existing_dict = {"Book_Price": 10.97,
                        "Book_Stars": 1,
                        "Book_Title": 'The Long Shadow',
                        "Book_total_category_amouth": 1
                        }
        # example 01 - only one Key to stay in new dict
        key_to_stay = "Book_Title"
        data= self.game.leave_only_selected_keys_in_existing_dict(existing_dict, key_to_stay)
        self.assertEqual(data, {'Book_Title': 'The Long Shadow'})

        # example 02- two Keys to stay in new dict
        data_2_keys = self.game.leave_only_selected_keys_in_existing_dict(existing_dict, "Book_Price", "Book_Stars")
        self.assertEqual(data_2_keys, {"Book_Price": 10.97,
                                       "Book_Stars": 1})

        # example 03- anything not sholud be change in existing dict 
        data_4_keys = self.game.leave_only_selected_keys_in_existing_dict(existing_dict, "Book_Price", "Book_Stars", "Book_Title", "Book_total_category_amouth")
        self.assertEqual(data_4_keys, {"Book_Price": 10.97,
                                       "Book_Stars": 1,
                                       "Book_Title": 'The Long Shadow',
                                       "Book_total_category_amouth": 1
                                       })

    def test_generate_tab_title_price(self):
        s2 = [{
            "Book_Available": True,
            "Book_Category": "Travel",
            "Book_First_Link": "https://books.toscrape.com/catalogue/category/books/travel_2/index.html",
            "Book_Price": 26.08,
            "Book_Stars": 5,
            "Book_Title": "1,000 Places to See Before You Die",
            "Book_total_category_amouth": 11
                },
            {
                "Book_Available": True,
                "Book_Category": "Mystery",
                "Book_First_Link": "https://books.toscrape.com/catalogue/category/books/mystery_3/index.html",
                "Book_Price": 47.82,
                "Book_Stars": 4,
                "Book_Title": "Sharp Objects",
                "Book_total_category_amouth": 32
            }]
        input_this_method_1_title= self.game.generate_tab_title_price(s2,["Sharp Objects"])
        self.assertEqual(input_this_method_1_title,[{'Book_Price': 47.82, 'Book_Title': 'Sharp Objects'}])

        input_this_method_1_another_title = self.game.generate_tab_title_price(s2,["1,000 Places to See Before You Die"])
        self.assertEqual(input_this_method_1_another_title, [{'Book_Price': 26.08, 'Book_Title': '1,000 Places to See Before You Die'}])

        input_this_method_3_another_titles = self.game.generate_tab_title_price(s2, ["Sharp Objects", "1,000 Places to See Before You Die"])
        self.assertEqual(input_this_method_3_another_titles, [{'Book_Price': 26.08, 'Book_Title': '1,000 Places to See Before You Die'},
                                                              {'Book_Price': 47.82, 'Book_Title': 'Sharp Objects'}])

        input_this_method_4_zero_title = self.game.generate_tab_title_price(s2, [])
        self.assertEqual(input_this_method_4_zero_title, [])


    def test_generate_tab_title_stars(self):
        s2 = [{
            "Book_Available": True,
            "Book_Category": "Travel",
            "Book_First_Link": "https://books.toscrape.com/catalogue/category/books/travel_2/index.html",
            "Book_Price": 26.08,
            "Book_Stars": 5,
            "Book_Title": "1,000 Places to See Before You Die",
            "Book_total_category_amouth": 11
                },
            {
                "Book_Available": True,
                "Book_Category": "Mystery",
                "Book_First_Link": "https://books.toscrape.com/catalogue/category/books/mystery_3/index.html",
                "Book_Price": 47.82,
                "Book_Stars": 4,
                "Book_Title": "Sharp Objects",
                "Book_total_category_amouth": 32
            }]
        input_this_method_1_title= self.game.generate_tab_title_stars(s2,["Sharp Objects"])
        self.assertEqual(input_this_method_1_title, [{'Book_Stars': 4, 'Book_Title': 'Sharp Objects'}])

        input_this_method_1_another_title = self.game.generate_tab_title_stars(s2, ["1,000 Places to See Before You Die"])
        self.assertEqual(input_this_method_1_another_title, [
                         {'Book_Stars': 5, 'Book_Title': '1,000 Places to See Before You Die'}])

        input_this_method_3_another_titles = self.game.generate_tab_title_stars(
            s2, ["Sharp Objects", "1,000 Places to See Before You Die"])
        self.assertEqual(input_this_method_3_another_titles, [{'Book_Stars': 5, 'Book_Title': '1,000 Places to See Before You Die'},
                                                              {'Book_Stars': 4, 'Book_Title': 'Sharp Objects'}])

        input_this_method_4_zero_title = self.game.generate_tab_title_stars(s2, [
        ])
        self.assertEqual(input_this_method_4_zero_title, [])

        
    def test_sort_method_1(self):
        # EXAMPLE 01
        list_dict_title_and_price = [{'Book_Price': 26.08, 'Book_Title': '1,000 Places to See Before You Die'},
                                     {'Book_Price': 47.82, 'Book_Title': 'Sharp Objects'}]
        
        first_input=self.game.sort_method_1(list_dict_title_and_price)
        self.assertEqual(first_input, [{'Book_Price': 47.82, 'Book_Title': 'Sharp Objects'},
                                       {'Book_Price': 26.08, 'Book_Title': '1,000 Places to See Before You Die'}])
        # EXAMPLE 02
        list_dict_title_and_price_imagine_data = [{'Book_Price': 0.00, 'Book_Title': '1,000 Places to See Before You Die'},
                                     {'Book_Price': 10000.00, 'Book_Title': 'Sharp Objects'}]

        second_input = self.game.sort_method_1(list_dict_title_and_price_imagine_data)
        self.assertEqual(second_input, [{'Book_Price': 10000.00, 'Book_Title': 'Sharp Objects'},
                                       {'Book_Price': 0.00, 'Book_Title': '1,000 Places to See Before You Die'}])
        
        # EXAMPLE 03
        list_dict_title_and_price_imagine_data_2 = [{'Book_Price': -90.00, 'Book_Title': '1,000 Places to See Before You Die'},
                                                  {'Book_Price': 10000.00, 'Book_Title': 'Sharp Objects'}]

        third_input = self.game.sort_method_1(list_dict_title_and_price_imagine_data_2)
        self.assertEqual(third_input, [{'Book_Price': 10000.00, 'Book_Title': 'Sharp Objects'},
                                        {'Book_Price': -90.00, 'Book_Title': '1,000 Places to See Before You Die'}])



    def test_sort_method_2(self):
        # EXAMPLE 01 
        list_dict_title_and_price = [{'Book_Price': 26.08, 'Book_Title': '1,000 Places to See Before You Die'},
                                     {'Book_Price': 47.82, 'Book_Title': 'Sharp Objects'}]
        
        first_input=self.game.sort_method_2(list_dict_title_and_price)
        self.assertEqual(first_input, [{'Book_Price': 26.08, 'Book_Title': '1,000 Places to See Before You Die'},
                                       {'Book_Price': 47.82, 'Book_Title': 'Sharp Objects'}])

    def test_sort_method_3(self):
        # EXAMPLE 01
        list_dict_only_title_AND_stars = [{'Book_Stars': 5, 'Book_Title': '1,000 Places to See Before You Die'},
                                     {'Book_Stars': 4, 'Book_Title': 'Sharp Objects'}]

        first_input = self.game.sort_method_3(list_dict_only_title_AND_stars)
        self.assertEqual(first_input, [{'Book_Stars': 5, 'Book_Title': '1,000 Places to See Before You Die'},
                                       {'Book_Stars': 4, 'Book_Title': 'Sharp Objects'}])

        # EXAMPLE 02 - imagine data
        list_dict_only_title_AND_stars_imagine_data = [{'Book_Stars': 5, 'Book_Title': '1,000 Places to See Before You Die'},
                                                  {'Book_Stars': 4, 'Book_Title': 'Sharp Objects'},
                                                  {'Book_Stars': 0, 'Book_Title': 'NEW TITLE 1,000 Places to See Before You Die'},
                                                  {'Book_Stars': 0, 'Book_Title': 'NEW TITLE Sharp Objects'}]

        second_input = self.game.sort_method_3(list_dict_only_title_AND_stars_imagine_data)
        self.assertEqual(second_input, [{'Book_Stars': 5, 'Book_Title': '1,000 Places to See Before You Die'},
                                        {'Book_Stars': 4, 'Book_Title': 'Sharp Objects'},
                                        {'Book_Stars': 0, 'Book_Title': 'NEW TITLE 1,000 Places to See Before You Die'},
                                        {'Book_Stars': 0, 'Book_Title': 'NEW TITLE Sharp Objects'}
        ])

    def test_sort_method_4(self):
            # EXAMPLE 01
        list_dict_only_title_AND_stars = [{'Book_Stars': 5, 'Book_Title': '1,000 Places to See Before You Die'},
                                          {'Book_Stars': 4, 'Book_Title': 'Sharp Objects'}]

        first_input = self.game.sort_method_4(list_dict_only_title_AND_stars)
        self.assertEqual(first_input, [{'Book_Stars': 4, 'Book_Title': 'Sharp Objects'},
                                      {'Book_Stars': 5, 'Book_Title': '1,000 Places to See Before You Die'}])

        # EXAMPLE 02 - imagine data
        list_dict_only_title_AND_stars_imagine_data = [{'Book_Stars': 5, 'Book_Title': '1,000 Places to See Before You Die'},
                                                       {'Book_Stars': 4, 'Book_Title': 'Sharp Objects'},
                                                       {'Book_Stars': 0, 'Book_Title': 'NEW TITLE 1,000 Places to See Before You Die'},
                                                       {'Book_Stars': 0, 'Book_Title': 'NEW TITLE Sharp Objects'}]

        second_input = self.game.sort_method_4(list_dict_only_title_AND_stars_imagine_data)
        self.assertEqual(second_input, [{'Book_Stars': 0, 'Book_Title': 'NEW TITLE Sharp Objects'},
                                        {'Book_Stars': 0, 'Book_Title': 'NEW TITLE 1,000 Places to See Before You Die'},
                                        {'Book_Stars': 4, 'Book_Title': 'Sharp Objects'},
                                        {'Book_Stars': 5, 'Book_Title': '1,000 Places to See Before You Die'}])


    def test_sort_method_5(self):
        list_titles = ["It's Only the Himalayas", 'Full Moon over Noah’s Ark: An Odyssey to Mount Ararat and Beyond', 'See America: A Celebration of Our National Parks & Treasured Sites', 'Vagabonding: An Uncommon Guide to the Art of Long-Term World Travel', 'Under the Tuscan Sun',
                        'A Summer In Europe', 'The Great Railway Bazaar', 'A Year in Provence (Provence #1)', 'The Road to Little Dribbling: Adventures of an American in Britain (Notes From a Small Island #2)', 'Neither Here nor There: Travels in Europe', '1,000 Places to See Before You Die']
        first_input = self.game.sort_method_5(list_titles)
        self.assertEqual(first_input, [ '1,000 Places to See Before You Die',
                                        'A Summer In Europe',
                                        'A Year in Provence (Provence #1)',
                                       'Full Moon over Noah’s Ark: An Odyssey to Mount Ararat and Beyond',
                                         "It's Only the Himalayas",
                                        'Neither Here nor There: Travels in Europe',
                                         'See America: A Celebration of Our National Parks & Treasured Sites',
                                         'The Great Railway Bazaar',
                                        'The Road to Little Dribbling: Adventures of an American in Britain (Notes '
                                        'From a Small Island #2)',
                                         'Under the Tuscan Sun',
                                        'Vagabonding: An Uncommon Guide to the Art of Long-Term World Travel'])
        
    def test_catch_index_if_have_title(self):
        s3 = [{
            "category": "Travel",
            "detals_link_to_book": "https://books.toscrape.com/catalogue/a-summer-in-europe_458/index.html",
            "in_stock_how_many_available": 7,
            "price": "\u00a344.34",
            "productDescription": "On her thirtieth birthday, Gwendolyn Reese receives an unexpected present from her widowed Aunt Bea: a grand tour of Europe in the company of Bea's Sudoku and Mahjongg Club. The prospect isn't entirely appealing. But when the gift she is expecting--an engagement ring from her boyfriend--doesn't materialize, Gwen decides to go. At first, Gwen approaches the trip as if it's On her thirtieth birthday, Gwendolyn Reese receives an unexpected present from her widowed Aunt Bea: a grand tour of Europe in the company of Bea's Sudoku and Mahjongg Club. The prospect isn't entirely appealing. But when the gift she is expecting--an engagement ring from her boyfriend--doesn't materialize, Gwen decides to go. At first, Gwen approaches the trip as if it's the math homework she assigns her students, diligently checking monuments off her must-see list. But amid the bougainvillea and stunning vistas of southern Italy, something changes. Gwen begins to live in the moment--skipping down stone staircases in Capri, running her fingers over a glacier in view of the Matterhorn, racing through the Louvre, and taste-testing pastries at a Marseilles cafe. Reveling in every new experience--especially her attraction to a charismatic British physics professor--Gwen discovers that the ancient wonders around her are nothing compared to the renaissance unfolding within. . . \"A thinking woman's love story, it swept me away to breathtaking places with a cast of endearing characters I won't soon forget. Bravissima!\" Susan McBride, author of \"Little Black Dress\" Praise for Marilyn Brant's According to Jane \"A warm, witty and charmingly original story.\" --Susan Wiggs, \"New York Times \" bestselling author \"Brant infuses her sweetly romantic and delightfully clever tale with just the right dash of Austen-esque wit.\" \"Chicago Tribune\" \"An engaging read for all who have been through the long, dark, dating wars, and still believe there's sunshine, and a Mr. Darcy, at the end of the tunnel.\" --Cathy Lamb, author of \"Such a Pretty Face\"\" ...more",
            "productInformation_UPC": "cc1936a9f4e93477",
            "title_book": "A Summer In Europe"
            },
                {
                "category": "Travel",
                "detals_link_to_book": "https://books.toscrape.com/catalogue/the-great-railway-bazaar_446/index.html",
                "in_stock_how_many_available": 6,
                "price": "\u00a330.54",
                "productDescription": "First published more than thirty years ago, Paul Theroux's strange, unique, and hugely entertaining railway odyssey has become a modern classic of travel literature. Here Theroux recounts his early adventures on an unusual grand continental tour. Asia's fabled trains -- the Orient Express, the Khyber Pass Local, the Frontier Mail, the Golden Arrow to Kuala Lumpur, the Mand First published more than thirty years ago, Paul Theroux's strange, unique, and hugely entertaining railway odyssey has become a modern classic of travel literature. Here Theroux recounts his early adventures on an unusual grand continental tour. Asia's fabled trains -- the Orient Express, the Khyber Pass Local, the Frontier Mail, the Golden Arrow to Kuala Lumpur, the Mandalay Express, the Trans-Siberian Express -- are the stars of a journey that takes him on a loop eastbound from London's Victoria Station to Tokyo Central, then back from Japan on the Trans-Siberian. Brimming with Theroux's signature humor and wry observations, this engrossing chronicle is essential reading for both the ardent adventurer and the armchair traveler. ...more",
                "productInformation_UPC": "48736df57e7bec9f",
                "title_book": "The Great Railway Bazaar"
            }]
        first_input = self.game.catch_index_if_have_title('A Summer In Europe',s3)
        self.assertEqual(first_input, 0)

        second_input = self.game.catch_index_if_have_title('The Great Railway Bazaar',s3)
        self.assertEqual(second_input, 1)

    def test_return_details(self):
        s3 = [{
            "category": "Travel",
            "detals_link_to_book": "https://books.toscrape.com/catalogue/a-summer-in-europe_458/index.html",
            "in_stock_how_many_available": 7,
            "price": "£44.34",
            "productDescription": "On her thirtieth birthday, Gwendolyn Reese receives an unexpected present",
            "productInformation_UPC": "cc1936a9f4e93477",
            "title_book": "A Summer In Europe"
            },
                {
                "category": "Travel",
                "detals_link_to_book": "https://books.toscrape.com/catalogue/the-great-railway-bazaar_446/index.html",
                "in_stock_how_many_available": 6,
                "price": "£44.34",
                "productDescription": "First published more than thirty years ago, Paul Theroux's strange, ...",
                "productInformation_UPC": "48736df57e7bec9f",
                "title_book": "The Great Railway Bazaar"
            }]

        first_input = self.game.return_details("A Summer In Europe",s3)
        self.assertEqual(
            first_input, ['A Summer In Europe',
                        'Travel',
                        '£44.34',
                        'On her thirtieth birthday, Gwendolyn Reese receives an unexpected present',
                        7,
                        'https://books.toscrape.com/catalogue/a-summer-in-europe_458/index.html',
                        'cc1936a9f4e93477'])
      



if __name__ == "__main__":
    unittest.main()

# RESULT 
"""
.............
----------------------------------------------------------------------
Ran 13 tests in 0.001s

OK
"""
