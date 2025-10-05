show_table_query = "DESCRIBE restaurants"
with connection.cursor() as cursor:
    cursor.execute(show_table_query)
    result = cursor.fetchall()
    for row in result:
        print(row)

