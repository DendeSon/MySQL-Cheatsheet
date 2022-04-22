# Changing data type from INT to DECIMAL for a column
alter_table_query = """
ALTER TABLE movies
MODIFY COLUMN collection_in_mil DECIMAL(4,1)
"""
# DECIMAL(4,1) means 4 DIGITS total and 1 DECIMAL place
show_table_query = "DESCRIBE movies"
with connection.cursor() as cursor:
    cursor.execute(alter_table_query)
    cursor.execute(show_table_query)
    # Fetch rows from last executed query
    result = cursor.fetchall()
    print("Movie Table Schema after alteration:")
    for row in result:
        print(row)

# Output
# ('id', 'int(11)', 'NO', 'PRI', None, 'auto_increment')
# ('title', 'varchar(100)', 'YES', '', None, '')
# ('release_year', 'year(4)', 'YES', '', None, '')
# ('genre', 'varchar(100)', 'YES', '', None, '')
# ('collection_in_mil', 'decimal(4,1)', 'YES', '', None, '')