import sqlite3
# import sys

db_file = 'sql.db'


class DB:
    """DBClient"""

    def generic_sql(self, query: str):
        # Establish a connection to the database
        conn = sqlite3.connect(db_file)

        # Create a cursor object to execute SQL commands
        cursor = conn.cursor()

        # Execute the SQL command
        cursor.execute(query)

        # Commit the transaction to save changes to the database
        conn.commit()

        # Fetch the result set
        result_set = cursor.fetchall()

        # Close the cursor and the database connection
        cursor.close()
        conn.close()

        # Return the result set
        return result_set

        # try:
        #     # Connect to DB and create a cursor
        #     sqliteConnection = sqlite3.connect('sql.db')
        #     cursor = sqliteConnection.cursor()

        #     cursor.execute(query)

        #     # Fetch and output result
        #     result = cursor.fetchall()
        #     return result

        #     # Close the cursor
        #     cursor.close()

        # # Handle errors
        # except sqlite3.Error as error:
        #     print('Error occurred - ', error)

        # # Close DB Connection irrespective of success
        # # or failure
        # finally:

        #     if sqliteConnection:
        #         sqliteConnection.close()
        #         print('SQLite Connection closed')

    def init_sqlite(self):
        createTable = """ CREATE TABLE links (
                        url TEXT,
                        status TEXT,
                        remark TEXT
                    );"""
        self.generic_sql(createTable)

    def save_link(self, url: str):
        query = f""" INSERT INTO links
                        (url)
                        VALUES('{url}');
                """
        print(query)
        self.generic_sql(query)

    # # sys.modules[__name__] = init_sqlite
