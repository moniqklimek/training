# Subject: Books - simulation of data flow from different sources and different formats

> File formats: .py, .csv,. ipynb
website: https: // books.toscrape.com/catalogue/category/books_1/index.html
used: Web Scraping, Driver, json, unittest, Class, Pandas, Jupyter Notebook, SQL

#####  I WEBSCRAPING - obtaining external data from a selected website 

-  SCRAPING 01
A. from the container: div.side_categories - catch:
    1. category titles
    2. link to the first thematic page

- SCRAPING 02
B. come from only thematic pages, and collect info such as: book availability, category, link to the thematic page from which the result was read, price, the number of stars, title, the number of books on a given topic

- SCRAPING 03
C. go to each detailed page, e.g. https://books.toscrape.com/catalogue/its-only-the-himalayas_981/index.html and read from it information such as: category, a detailed link that allows you to open this page at any time, how many are available in stock, cash desk price, a short summary of the book, inf about the product - i.e. UPC designation  

-  ✨  - NOTE: data collected independently of each other, intentionally duplicated to present the possibilities of collecting data from each page 


#####  II - CHECK the correctness of the data read from the website
-   checking the correctness of the generated files based on the comparison:
- results from the website,
- and the corresponding results obtained from the analysis of json files and the dictionaries contained therein
-  ✨  - NOTE: djust started the topic

##### III LOGIC FLOW - how to practically use the previously obtained data 
###### and use them by reading from json files to a program that downloads current results from the User input  and manages the flow of information in the program

-  ✨  - LOGIC
- 100. Ask the user what category of prince interests him(show him the sorted results)
- 101. enter the selected category and ask if User wants to sort them by:
    - increasing price,
    - decreasing price,
    - the highest number of stars,
    - the lowest number of stars,
    - availability,
and present the results
-   102. The user has chosen a given book - show him a short description and product description 
-  ✨  - NOTE: the program has not been secured against incorrect User responses
it was assumed that the answers will be entered correctly, according to the legend, with capital letters, no unnecessary spaces, etc.

#####  IV -  data visualization module Pandas
- data cleaning, grouping, filtering,
- graphic visualization of the results,
- translating SQL queries

##### FILES:
resources:
```sh
01_category_first_link.json
02_single_books.json
03_details_single_books.json

02.csv
```
src:
```sh
scraping_text.py
analysis_data_from_scraping.py
game.py

books.ipynb
```
test:
```sh
scraping_text_test.py
analysis_data_from_scraping_test.py
game_test.py
```



##### Files:

| part | I WEBSCRAPING |comments |
| ------ | ------ | ------ |
| code | "scraping_text.py"| |
| tests | "scraping_text_test.py" | -> Ran 5 tests in 0.001s OK 
| result | 3 jsons files |"01_category_first_link.json" ,"02_single_books.json","03_details_single_books.json"

| part | II  CHECK WEBSCRAPING  |
| ------ | ------ |
| code | "analiza_danych_ze_scrapingu.py"| 

| part | III LOGIC FLOW |comments |
| ------ | ------ | ------ |
| code | "game.py"| |
| tests | "game_test.py"  | Ran 13 tests in 0.001s OK 
| result | interaktive game with User| use of the Terminal console 

| part | IV analysis  |
| ------ | ------ |
| code | books.ipynb | 


| Oprogramowanie | version |
| ------ | ------ |
| Python | 3.7.6 64 bit |
| IDE: Visual Studio Code | 1.53.2 |
| macOS Big Sure|  11.2.1 |

##### Inne: 
-  metodyka: TDD - Test-driven development
##### Author : 
- Monika Klimek
##### Creation date: 
- 20-22.03.2021
