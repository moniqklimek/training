"""
generate file format .csv from WebScraping and json
"""
import pandas as pd
from csv import DictWriter
import json 


# change '02_single_books.json' -->'02.csv'
df = pd.read_json('resources/02_single_books.json')
df.to_csv('resources/02.csv', index= None) 


