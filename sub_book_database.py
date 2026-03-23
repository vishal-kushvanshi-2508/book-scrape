


from store_data_database import *

product_table_name = "product_detail"


def fetch_product_table_data():
    connection = get_connection()
    cursor = connection.cursor()
    query = f"SELECT id, website_link FROM {product_table_name};"
    cursor.execute(query)

    rows = cursor.fetchall()

    result = []

    for row in rows:
        data = {
            "id": row[0],
            "website_link": row[1]
            # "status": row[2]
        }
        result.append(data)

    cursor.close()
    connection.close()
    return result

