from mysql.connector import connect, Error


def create_db():
    try:
        with connect(
            host="localhost",
            port="3306",
            user="root",
            password="pass",
        ) as connection:
            create_db_query = "CREATE DATABASE IF NOT EXISTS parsing"
            with connection.cursor() as cursor:
                cursor.execute(create_db_query)
                print('-> DB "parsing" was created')
    except Error as e:
        print(f'-! Error: {e}')


def create_table():
    try:
        with connect(
            host="localhost",
            port="3306",
            user="root",
            password="pass",
            database="parsing"
        ) as connection:
            create_table_query = """
                CREATE TABLE IF NOT EXISTS parsed_data (
                id INT NOT NULL AUTO_INCREMENT,
                PRIMARY KEY (id),
                page_id INT,
                image VARCHAR(128),
                title VARCHAR(64),
                date VARCHAR(10),
                location VARCHAR(16),
                beds VARCHAR(16),
                description TEXT,
                price FLOAT,
                currency VARCHAR(1)
                )
            """
            with connection.cursor() as cursor:
                cursor.execute(create_table_query)
                print('-> Table "parsed_data" was created')
    except Error as e:
        print(f'-! Error: {e}')


def insert(rows):
    try:
        with connect(
            host="localhost",
            port="3306",
            user="root",
            password="pass",
            database="parsing"
        ) as connection:
            insert_query = """
                INSERT INTO parsed_data (page_id, image, title, date, location, beds, description, price, currency)
                VALUES (%s, %s, %s, %s, %s, %s, %s, %s, %s)
            """
            with connection.cursor() as cursor:
                cursor.executemany(insert_query, rows)
                connection.commit()
                print('+ Records inserted successfully')
    except Error as e:
        print(f'-! Error: {e}')


def show():
    try:
        with connect(
            host="localhost",
            port="3306",
            user="root",
            password="pass",
            database="parsing"
        ) as connection:
            select_query = """
                SELECT * FROM parsed_data
            """
            with connection.cursor() as cursor:
                print('Here your data:')
                cursor.execute(select_query)
                records = cursor.fetchall()
                for row in records:
                    print(row)

    except Error as e:
        print(f'-! Error: {e}')


def drop_table():
    try:
        with connect(
            host="localhost",
            port="3306",
            user="root",
            password="pass",
            database="parsing"
        ) as connection:
            drop_query = """
                DROP TABLE parsed_data
            """
            with connection.cursor() as cursor:
                print('-> Table "parsed_data" was dropped')
                cursor.execute(drop_query)
    except Error as e:
        print(f'-! Error: {e}')


if __name__ == '__main__':
    create_db()
    create_table()
    # drop_table()
    show()
