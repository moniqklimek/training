from scraping_text import Books
from scraping_text import Single_Book

import unittest

"""
assumption : methods tests without going to the website
"""


class BooksTest(unittest.TestCase):
    def setUp(self):
        self.books = Books()

    def test_catch_category_and_first_link(self):
        pass

    def test_catch_change_string_rating_description_to_int(self):
        check = self.books.change_string_rating_description_to_int('Three')
        self.assertEqual(check, 3)

    def test_create_all_links_for_single_category(self):
        positive_example = self.books.create_all_links_for_single_category('https://books.toscrape.com/catalogue/category/books/mystery_3/index.html', 32)
     

        self.assertEqual(positive_example, ['https://books.toscrape.com/catalogue/category/books/mystery_3/index.html','https://books.toscrape.com/catalogue/category/books/mystery_3/page-2.html'])
        
        positive_example = self.books.create_all_links_for_single_category(
            'https://books.toscrape.com/catalogue/category/books/travel_2/index.html', 11)
        self.assertEqual(positive_example, ['https://books.toscrape.com/catalogue/category/books/travel_2/index.html'])
        self.assertEqual(len(positive_example),1)

        negative_example = self.books.create_all_links_for_single_category(
            'https://books.toscrape.com/catalogue/category/books/mystery_3/index.html', 32)
        self.assertNotEqual(negative_example, ['https://books.toscrape.com/catalogue/category/books/mystery_3/index.html'])

        


class Single_BookTest(unittest.TestCase):
    def setUp(self):
        self.single_book = Single_Book()

    def test_change_str_available_and_get_value_only(self):
        a = self.single_book.change_str_available_and_get_value_only('In stock (19 available)')
        self.assertEqual(a,19)
    
          
    def test_create_set_with_link_to_category_side(self):
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
                "Book_Title": "Full Moon over Noah\u2019s Ark: An Odyssey to Mount Ararat and Beyond",
                "Book_total_category_amouth": 11
            }]
        new_data=self.single_book.create_set_with_link_to_category_side(s2)
        self.assertEqual(new_data, {"https://books.toscrape.com/catalogue/category/books/travel_2/index.html"})

        s2_a = [
            {
                "Book_Available": True,
                "Book_Category": "Travel",
                "Book_First_Link": 'https://books.toscrape.com/catalogue/category/books/travel_2/index.html',
                "Book_Price": 26.08,
                "Book_Stars": 5,
                "Book_Title": "1,000 Places to See Before You Die",
                "Book_total_category_amouth": 11
            },
            {
                "Book_Available": True,
                "Book_Category": "Mystery",
                "Book_First_Link": 'https://books.toscrape.com/catalogue/category/books/mystery_3/index.html',
                "Book_Price": 47.82,
                "Book_Stars": 4,
                "Book_Title": "Sharp Objects",
                "Book_total_category_amouth": 32
            }]
        
        new_data = self.single_book.create_set_with_link_to_category_side(s2)
        # the elements of the set do not have a fixed position, it cannot be checked here -- assertEqual
        # change assertEqual--> assertTrue
        self.assertTrue(new_data, {'https://books.toscrape.com/catalogue/category/books/mystery_3/index.html', 'https://books.toscrape.com/catalogue/category/books/travel_2/index.html'})
        

if __name__ == "__main__":
    unittest.main()
