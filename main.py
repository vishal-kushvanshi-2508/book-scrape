
from extract_data import *
import time
from store_data_database import *
from pages_request_city_data import *

from sub_book_database import *

# file_name = "Domino's Pizza Restaurants in Mumbai _ Nearby Pizza Shops in Mumbai – Domino’s India.html"
base_url = "https://books.toscrape.com/"

def main():
    ## city name and url for table crate
    create_table_books()
    print("table created")
    
    # create url list and status default pending
    book_url_list = generate_url(base_url)

    # insert url data in table
    books_url_insert(list_data=book_url_list)
    
    # fetch book url data
    book_data_list = fetch_table_data()

    # create table for product.    
    create_table_product()

    # create html file and extract pages data.
    create_html_files(book_data_list)


    ## sub book start code .
    
    # fetch product data.
    product_data_list = fetch_product_table_data()
    print(product_data_list)




if __name__ == "__main__":
    start = time.time()
    main()

    end = time.time()
    print("time different  : ", end - start)


