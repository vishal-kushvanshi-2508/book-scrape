


from store_data_database import *

# product_table_name = "product_detail"


def fetch_sub_book_table_data():
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



### sub book table code 

sub_book_table_name = "sub_book_detail"


def create_table_sub_book():
    connection = get_connection()
    cursor = connection.cursor()

    ## delete table if exist ....
    delete_query = f"DROP TABLE IF EXISTS {sub_book_table_name};"
    cursor.execute(delete_query)

    try:
        query =  f"""
                CREATE TABLE IF NOT EXISTS {sub_book_table_name}(
                id INT AUTO_INCREMENT PRIMARY KEY,
                book_name VARCHAR(500) ,
                price VARCHAR(150) ,
                image_url TEXT,
                available VARCHAR(150), 
                description TEXT,
                upc VARCHAR(150) ,
                product_type VARCHAR(150) ,
                price_with_exclude VARCHAR(150) ,
                price_with_include VARCHAR(150) ,
                tax VARCHAR(150) ,
                number_reviews VARCHAR(150) 
        ); """
        cursor.execute(query)
        connection.commit()
    except Exception as e:
        print("Table creation failed")
        if connection:
            connection.rollback()
    finally:
        if cursor:
            cursor.close()
        if connection:
            connection.close()




def sub_book_data_insert(list_data : list):
    connection = get_connection()
    cursor = connection.cursor()
    dict_data = list_data[0]
    columns = ", ".join(list(dict_data.keys()))
    values = "".join([len(dict_data.keys()) * '%s,']).strip(',')
    parent_sql = f"""INSERT INTO {sub_book_table_name} ({columns}) VALUES ({values})"""
    try:
        product_values = []
        for dict_data in list_data:
            product_values.append( (
                dict_data.get("book_name") ,
                dict_data.get("price") ,
                dict_data.get("image_url") ,
                dict_data.get("available") ,
                dict_data.get("description") ,
                dict_data.get("upc") ,
                dict_data.get("product_type") ,
                dict_data.get("price_with_exclude") ,
                dict_data.get("price_with_include") ,
                dict_data.get("tax") ,
                dict_data.get("number_reviews") 
            ))

        try:
            batch_count = data_commit_batches_wise(connection, cursor, parent_sql, product_values)
            print(f"Parent batches executed count={batch_count}")
        except Exception as e:
            print(f"batch can not. Error : {e} ")

        cursor.close()
        connection.close()

    except Exception as e:
        ## this exception execute when error occur in try block and rollback until last save on database .
        connection.rollback()
        # print(f"Transaction failed, rolled back. Error: {e}")
        print("Transaction failed. Rolling back")
    except:
        print("except error raise ")
    finally:
        connection.close()





