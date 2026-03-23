



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