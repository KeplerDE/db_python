"""CREATE TABLE "Seat" (
	"seat_id"	TEXT,
	"taken"	INTEGER,
	"price"	REAL
)"""
import sqlite3



import sqlite3

connection = sqlite3.connect("cinema.db")   # connectiom to instance
connection.execute("""
    CREATE TABLE "Seat" (
	    "seat_id"	TEXT,
	    "taken"	INTEGER,
	    "price"	REAL
	    );
	    
	    """)
connection.commit()
connection.close()