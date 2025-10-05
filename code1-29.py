insert_restaurants_query = """
INSERT INTO restaurants
(name, type, rating)
VALUES ( %s, %s )
"""
reviewers_records = [
    ("My Mexican Restaurant", "Mexican", 5.4),
    ("The Italian One", "Italian", 8.3),
]
with connection.cursor() as cursor:
    cursor.executemany(insert_restaurants_query, reviewers_records)
    connection.commit()

