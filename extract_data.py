

from lxml import html


# get html content using url

def generate_url(base_url):
    book_url_list = []
    book_url_list.append( {
            "website_link" : base_url,
            "status" : "pending"
        })
    for page in range(2,51):
        book_url_list.append( {
            "website_link" : base_url + f"catalogue/page-{page}.html",
            "status" : "pending"
        })

    return book_url_list

