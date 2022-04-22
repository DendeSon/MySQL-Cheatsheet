# Show table schema
show_table_query = "DESCRIBE movies"
with connection.cursor() as cursor:
    cursor.execute(show_table_query)
    # Fetch rows from last executed query
    result = cursor.fetchall()
    for row in result:
        print(row)

# Use fetchall() to get ALL rows from the table


# Output
# ('id', 'int(11)', 'NO', 'PRI', None, 'auto_increment')
# ('title', 'varchar(100)', 'YES', '', None, '')
# ('release_year', 'year(4)', 'YES', '', None, '')
# ('genre', 'varchar(100)', 'YES', '', None, '')
# ('collection_in_mil', 'int(11)', 'YES', '', None, '')