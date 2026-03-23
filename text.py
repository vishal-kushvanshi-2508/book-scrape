


import os
import requests

from lxml import html

from store_data_database import product_data_insert

from store_data_database import *




def extract_data_from_html(html_content):
    book_list = []
    dict_data = {}

    base_url = "https://books.toscrape.com/"

    tree = html.fromstring(html_content)

    dict_data["book_name"] = tree.xpath(".//div[@class='col-sm-6 product_main']//h1/text()")[0].strip()

    dict_data["price"] = tree.xpath(".//div[@class='col-sm-6 product_main']//p[@class='price_color']/text()")[0].strip()

    dict_data["image_url"] = base_url + tree.xpath(".//div[@class='item active']//img/@src")[0].replace("../../", "")

    dict_data["available"] = tree.xpath(".//div[@class='col-sm-6 product_main']//p[@class='instock availability']/text()")[1].replace("\n", "").strip()

    dict_data["description"] = tree.xpath(".//div[@id='product_description']/following-sibling::p[1]/text()")[0]

    dict_data["upc"] = tree.xpath("//table[@class='table table-striped']//tr//td")[0].text

    dict_data["product_type"] = tree.xpath("//table[@class='table table-striped']//tr//td")[1].text

    dict_data["price_with_exclude"] = tree.xpath("//table[@class='table table-striped']//tr//td")[2].text
    
    dict_data["price_with_include"] = tree.xpath("//table[@class='table table-striped']//tr//td")[3].text

    dict_data["tax"] = tree.xpath("//table[@class='table table-striped']//tr//td")[4].text

    dict_data["number_reviews"] = tree.xpath("//table[@class='table table-striped']//tr//td")[6].text

    book_list.append(dict_data)
    print(book_list)

    return book_list




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

book_url = "https://books.toscrape.com/catalogue/the-complete-maus-maus-1-2_62/index.html"
response = requests.get(book_url, headers=headers, timeout=10)


# with open("html_content.html", "w", encoding="utf-8") as f:
#     f.write(response.text)


extract_data_from_html(response.text)
