from pprint import pprint

import mysql.connector

import board

db = mysql.connector.connect(
    host='localhost',
    user='root',
    passwd='secureminimono',
    database='secure_mini_mono'
)

# Display with condition
def select_query(query, values):
    select_cursor = db.cursor()
    select_cursor.execute(query, values)

    rows = select_cursor.fetchall()

    return rows


# Display all
def select_all_query(query):
    select_all_cursor = db.cursor()
    select_all_cursor.execute(query)

    rows = select_all_cursor.fetchall()

    return rows



def insertion_query(query, values):
    insertion_cursor = db.cursor()
    insertion_cursor.execute(query, values)

    db.commit()

    # This part just replies with a successful or not, not really important tbh
    if insertion_cursor.rowcount == 1:
        return True

    else:
        return False