create_restaurant_table_query = """
CREATE TABLE restaurants(
    id INT AUTO_INCREMENT PRIMARY KEY,
    name VARCHAR(100),
    type VARCHAR(100),
    Rating int(3)
)
"""
with connection.cursor() as cursor:
    cursor.execute(create_restaurant_table_query)
    connection.commit()

