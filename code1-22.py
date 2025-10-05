from getpass import getpass
from mysql.connector import connect, Error

try:
    with connect(
        host="localhost",
        port=3360,
        user=input("Enter username: "),
        password=getpass("Enter password: "),
    ) as connection:
        print(connection)
except Error as e:
    print(e)

