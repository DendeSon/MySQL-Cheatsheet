# Read all columns with LIMIT
select_movies_query = "SELECT * FROM movies LIMIT 5"
with connection.cursor() as cursor:
    cursor.execute(select_movies_query)
    result = cursor.fetchall()
    for row in result:
        print(row)

# Output
# (1, 'Forrest Gump', 1994, 'Drama', Decimal('330.2'))
# (2, '3 Idiots', 2009, 'Drama', Decimal('2.4'))
# (3, 'Eternal Sunshine of the Spotless Mind', 2004, 'Drama', Decimal('34.5'))
# (4, 'Good Will Hunting', 1997, 'Drama', Decimal('138.1'))
# (5, 'Skyfall', 2012, 'Action', Decimal('304.6'))



# Read selected columns with LIMIT
select_movies_query = "SELECT title, release_year FROM movies LIMIT 5"
with connection.cursor() as cursor:
    cursor.execute(select_movies_query)
    for row in cursor.fetchall():
        print(row)

# Output
# ('Forrest Gump', 1994)
# ('3 Idiots', 2009)
# ('Eternal Sunshine of the Spotless Mind', 2004)
# ('Good Will Hunting', 1997)
# ('Skyfall', 2012)



# Filter reading of columns
select_movies_query = """
SELECT title, collection_in_mil
FROM movies
WHERE collection_in_mil > 300
ORDER BY collection_in_mil DESC
"""
with connection.cursor() as cursor:
    cursor.execute(select_movies_query)
    for movie in cursor.fetchall():
        print(movie)

# Output
# ('Avengers: Endgame', Decimal('858.8'))
# ('Titanic', Decimal('659.2'))
# ('The Dark Knight', Decimal('535.4'))
# ('Toy Story 4', Decimal('434.9'))
# ('The Lion King', Decimal('423.6'))
# ('Deadpool', Decimal('363.6'))
# ('Forrest Gump', Decimal('330.2'))
# ('Skyfall', Decimal('304.6'))



# Concatenation
select_movies_query = """
SELECT CONCAT(title, " (", release_year, ")"),
      collection_in_mil
FROM movies
ORDER BY collection_in_mil DESC
LIMIT 5
"""
with connection.cursor() as cursor:
    cursor.execute(select_movies_query)
    for movie in cursor.fetchall():
        print(movie)

# Output
# ('Avengers: Endgame (2019)', Decimal('858.8'))
# ('Titanic (1997)', Decimal('659.2'))
# ('The Dark Knight (2008)', Decimal('535.4'))
# ('Toy Story 4 (2019)', Decimal('434.9'))
# ('The Lion King (1994)', Decimal('423.6'))



# Using .fetchmany(size=x) instead of LIMIT
select_movies_query = """
SELECT CONCAT(title, " (", release_year, ")"),
      collection_in_mil
FROM movies
ORDER BY collection_in_mil DESC
"""
with connection.cursor() as cursor:
    cursor.execute(select_movies_query)
    for movie in cursor.fetchmany(size=5):
        print(movie)
    cursor.fetchall() # <- .fetchall() used to clear unread results from .fetchmany(). If not used; will result in Error if on same connection

# Output
# ('Avengers: Endgame (2019)', Decimal('858.8'))
# ('Titanic (1997)', Decimal('659.2'))
# ('The Dark Knight (2008)', Decimal('535.4'))
# ('Toy Story 4 (2019)', Decimal('434.9'))
# ('The Lion King (1994)', Decimal('423.6'))