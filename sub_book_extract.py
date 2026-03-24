
from lxml import html
from sub_book_database import *


def extract_sub_book_data(html_content):
    sub_book_list = []
    dict_data = {}

    base_url = "https://books.toscrape.com/"

    tree = html.fromstring(html_content)

    dict_data["book_name"] = tree.xpath(".//div[@class='col-sm-6 product_main']//h1/text()")[0].strip()

    dict_data["price"] = tree.xpath(".//div[@class='col-sm-6 product_main']//p[@class='price_color']/text()")[0].strip()

    dict_data["image_url"] = base_url + tree.xpath(".//div[@class='item active']//img/@src")[0].replace("../../", "")

    dict_data["available"] = tree.xpath(".//div[@class='col-sm-6 product_main']//p[@class='instock availability']/text()")[1].replace("\n", "").strip()

    desc = tree.xpath(".//div[@id='product_description']/following-sibling::p[1]/text()")
    dict_data["description"] = desc[0].strip() if desc else None

    dict_data["upc"] = tree.xpath("//table[@class='table table-striped']//tr//td")[0].text

    dict_data["product_type"] = tree.xpath("//table[@class='table table-striped']//tr//td")[1].text

    dict_data["price_with_exclude"] = tree.xpath("//table[@class='table table-striped']//tr//td")[2].text
    
    dict_data["price_with_include"] = tree.xpath("//table[@class='table table-striped']//tr//td")[3].text

    dict_data["tax"] = tree.xpath("//table[@class='table table-striped']//tr//td")[4].text

    dict_data["number_reviews"] = tree.xpath("//table[@class='table table-striped']//tr//td")[6].text

    sub_book_list.append(dict_data)

    return sub_book_list





import os
import requests
from concurrent.futures import ThreadPoolExecutor, as_completed


# # ---------- WORKER FUNCTION ----------

import requests
from requests.adapters import HTTPAdapter
from urllib3.util.retry import Retry

def create_session():
    session = requests.Session()

    retries = Retry(
        total=3,
        backoff_factor=0.5,
        status_forcelist=[500, 502, 503, 504],
    )

    adapter = HTTPAdapter(max_retries=retries)
    session.mount("http://", adapter)
    session.mount("https://", adapter)

    return session


import time
import random

def process_sub_book(sub_book, headers, folder_path):
    session = create_session()  
    book_id = sub_book["id"]
    book_url = sub_book["website_link"]

    try:
        time.sleep(random.uniform(0.3, 0.8)) 

        response = session.get(
            book_url,
            headers=headers,
            timeout=15
        )

        if response.status_code != 200:
            print(f"Failed: {book_url} ({response.status_code})")
            return []

        file_path = os.path.join(folder_path, f"{book_id}_sub_book.html.gz")

        with open(file_path, "w", encoding="utf-8") as f:
            f.write(response.text)

        return extract_sub_book_data(response.text)

    except Exception as e:
        print(f"Error for {book_url}: {e}")
        return []




# ---------- MAIN FUNCTION ----------
def create_sub_book_html_files(sub_book_data_list):

    folder_path = r"D:/vishal_kushvanshi/book_scrape_sub_book/"

    headers = {
        'accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.7',
        'accept-language': 'en-US,en;q=0.9',
        'cache-control': 'no-cache',
        'pragma': 'no-cache',
        'priority': 'u=0, i',
        'referer': 'https://stores.burgerking.in/location/haryana',
        'sec-ch-ua': '"Not:A-Brand";v="99", "Google Chrome";v="145", "Chromium";v="145"',
        'sec-ch-ua-mobile': '?0',
        'sec-ch-ua-platform': '"Windows"',
        'sec-fetch-dest': 'document',
        'sec-fetch-mode': 'navigate',
        'sec-fetch-site': 'same-origin',
        'sec-fetch-user': '?1',
        'upgrade-insecure-requests': '1',
        'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/145.0.0.0 Safari/537.36'
    }

    sub_book_all_data_list = []

    with ThreadPoolExecutor(max_workers=10) as executor:
        futures = [
            executor.submit(process_sub_book, sub_book, headers,  folder_path)
            for sub_book in sub_book_data_list
        ]

        for future in as_completed(futures):
            
            result = future.result()   # list from each thread
            sub_book_all_data_list.extend(result)

    # insert after all threads complete
    if sub_book_all_data_list:
        sub_book_data_insert(list_data=sub_book_all_data_list)

    print("Total sub book records add :", len(sub_book_all_data_list))


















### method 2 to create html and store data

# def process_sub_book(sub_book, headers, folder_path):
#     book_id = sub_book["id"]
#     book_url = sub_book["website_link"]

#     try:
#         response = requests.get(book_url, headers=headers, timeout=30)

#         if response.status_code != 200:
#             print(f"Failed: {book_url} ({response.status_code})")
#             return []

#         # safe filename
#         file_path = os.path.join(folder_path, f"{book_id}_sub_book.html.gz")

#         # save html
#         with open(file_path, "w", encoding="utf-8") as f:
#             f.write(response.text)

#         # extract data
#         sub_book_list = extract_sub_book_data(response.text)

#         return sub_book_list

#     except Exception as e:
#         print(f"Error for {book_url}: {e}")
#         return []




# # ---------- MAIN FUNCTION ----------
# def create_sub_book_html_files(sub_book_data_list):

#     folder_path = r"D:/vishal_kushvanshi/book_scrape_sub_book/"

#     headers = {
#         'accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.7',
#         'accept-language': 'en-US,en;q=0.9',
#         'cache-control': 'no-cache',
#         'pragma': 'no-cache',
#         'priority': 'u=0, i',
#         'referer': 'https://stores.burgerking.in/location/haryana',
#         'sec-ch-ua': '"Not:A-Brand";v="99", "Google Chrome";v="145", "Chromium";v="145"',
#         'sec-ch-ua-mobile': '?0',
#         'sec-ch-ua-platform': '"Windows"',
#         'sec-fetch-dest': 'document',
#         'sec-fetch-mode': 'navigate',
#         'sec-fetch-site': 'same-origin',
#         'sec-fetch-user': '?1',
#         'upgrade-insecure-requests': '1',
#         'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/145.0.0.0 Safari/537.36'
#     }

#     sub_book_all_data_list = []

#     # Thread pool
#     with ThreadPoolExecutor(max_workers=10) as executor:

#         futures = [
#             executor.submit(process_sub_book, sub_book, headers, folder_path)
#             for sub_book in sub_book_data_list
#         ]
        
#         for future in as_completed(futures):
            
#             result = future.result()   # list from each thread
#             sub_book_all_data_list.extend(result)

#     # insert after all threads complete
#     if sub_book_all_data_list:
#         sub_book_data_insert(list_data=sub_book_all_data_list)

#     print("Total sub book records add :", len(sub_book_all_data_list))
