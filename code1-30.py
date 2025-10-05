select_restaurants_query = """
SELECT name, rating
FROM restaurants
WHERE rating > 2
ORDER BY rating ASC"""
with connection.cursor() as cursor:
    cursor.execute(select_restaurants_query)
    for name in cursor.fetchall():
        print(name)

