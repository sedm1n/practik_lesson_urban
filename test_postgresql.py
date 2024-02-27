import psycopg2

parametrs = {
    'host':'localhost',
    'port':5432,
    'dbname':'learndb',
    'password':'test1',
    'user':'pycharm'
}


try:
    # Connect to database
    connection = psycopg2.connect(**parametrs)
    connection.autocommit = True
    # The cursor to exist database
    with connection.cursor() as cursor:
        cursor.execute(
            "SELECT version()"
        )
        print("Server version {}".format(cursor.fetchone()))
    # Create new table
    # with connection.cursor() as cursor:
    #     cursor.execute(
    #         """CREATE TABLE users(
    #         id serial PRIMARY KEY,
    #         firt_name varchar(50) NOT NULL,
    #         nikname varchar(40))"""
    #     )

    # with connection.cursor() as cursor:
    #     cursor.execute(
    #         """
    #         INSERT INTO users (firt_name, nikname) VALUES
    #         ('Okeg', 'Baracuda');
    #         """
    #     )
    #     print('Insert ')
    with connection.cursor() as cursor:
        cursor.execute(
            "SELECT nikname FROM users WHERE firt_name = 'Okeg';"
        )
        print(cursor.fetchone())
    with connection.cursor() as cursor:
        cursor.execute(
            "DROP TABLE users;"
        )
except Exception as ex:
    print("Error ", ex)
finally:
    if connection:
        connection.close()
        print("Connection close")
    pass