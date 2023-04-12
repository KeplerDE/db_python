"""CREATE TABLE "Seat" (
	"seat_id"	TEXT,
	"taken"	INTEGER,
	"price"	REAL
)"""

import sqlite3


# connection = sqlite3.connect("cinema.db")  # connection to instance
# connection.execute("""
#     CREATE TABLE "Seat" (
# 	    "seat_id"	TEXT,
# 	    "taken"	INTEGER,
# 	    "price"	REAL
# 	    );
#
# 	    """)
# connection.commit()
# connection.close()


def insert_record():
    connection = sqlite3.connect("cinema.db")
    connection.execute("""
    INSERT INTO "Seat" ("seat_id", "taken", "price") VALUES ("A1", "0", "90"), ("A2", "1", "100"), ("A3", "0", "80")
    """)
    connection.commit()
    connection.close()


def select_all():
    connection = sqlite3.connect("cinema.db")
    cursor = connection.cursor()
    cursor.execute("""
    SELECT * FROM "Seat"
    """)
    result = cursor.fetchall()
    connection.close()
    return result

def select_specific_columns():
    connection = sqlite3.connect("cinema.db")
    cursor = connection.cursor()
    cursor.execute("""
    SELECT "seat_id", "price" FROM "Seat"
    """)
    result = cursor.fetchall()
    connection.close()
    return result

def select_with_condition():
    connection = sqlite3.connect("cinema.db")
    cursor = connection.cursor()
    cursor.execute("""
    SELECT "seat_id", "price" FROM "Seat" WHERE "price">80
    """)
    result = cursor.fetchall()
    connection.close()
    return result


# insert_record()

# print(select_all())
# print(select_specific_columns())
print(select_with_condition())
