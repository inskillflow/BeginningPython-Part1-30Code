from getpass import getpass
from mysql.connector import connect, Error

try:
    with connect(
        host="localhost",
        port=3306,
        user=input("Enter username: "),
        password=getpass("Enter password: "),
    ) as connection:
        create_db_query = "SHOW DATABASES"
        with connection.cursor() as cursor:
            #cursor = connection.cursor(buffered=True)
            cursor.execute(create_db_query)
except Error as e:
    print(e)

