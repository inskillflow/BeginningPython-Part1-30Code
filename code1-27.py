alter_table_query = """
ALTER TABLE restaurants
MODIFY COLUMN rating DECIMAL(4,1)
"""
show_table_query = "DESCRIBE restaurants"
with connection.cursor() as cursor:
    cursor.execute(alter_table_query)
    cursor.execute(show_table_query)
    # Fetch rows from last executed query
    result = cursor.fetchall()
    print("Restaurant Table Schema after alteration:")
    for row in result:
        print(row)

