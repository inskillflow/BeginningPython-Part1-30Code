drop_table_query = "DROP TABLE restaurants"
with connection.cursor() as cursor:
    cursor.execute(drop_table_query)

