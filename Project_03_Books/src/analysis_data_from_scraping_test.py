from analysis_data_from_scraping import Date
import unittest
import os
import sys





class DateTest(unittest.TestCase):
    def setUp(self):
        self.date = Date()

    def test_count_books_in_every_category(self):
        dictionary = self.date.count_books_in_every_category(
            [{'Book_Available': True, 
            'Book_Category': 'Travel', 
            'Book_First_Link': 'https://books.toscrape.com/catalogue/category/books/travel_2/index.html', 
            'Book_Price': 45.17, 
            'Book_Stars': 2, 
            'Book_Title': 
            "It's Only the Himalayas", 
            'Book_total_category_amouth': 11}, 

            {'Book_Available': True,
            'Book_Category': 'Travel', 
            'Book_First_Link': 'https://books.toscrape.com/catalogue/category/books/travel_2/index.html',
             'Book_Price': 49.43, 
             'Book_Stars': 4, 
             'Book_Title': 'Full Moon over Noah’s Ark: An Odyssey to Mount Ararat and Beyond',
              'Book_total_category_amouth': 11}
              ]
        )
        self.assertEqual(dictionary,  {'Travel': 2})
        #NOT
        self.assertNotEqual(dictionary,  {'Mystery': 2})
        self.assertNotEqual(dictionary,  {'Travel': 0})

        dictionary2 = self.date.count_books_in_every_category(
            [
             ]
        )
        self.assertNotEqual(dictionary2,  {'Travel': 2})


if __name__ == "__main__":
    unittest.main()
