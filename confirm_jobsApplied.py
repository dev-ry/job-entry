import sqlite3

# connect to database
con = sqlite3.connect("jobs_applied.db")


# create cursor
cur = con.cursor()

# execute query
cur.execute("select * from jobs_applied")
rows = cur.fetchall()

# loop the cursor to view the fetchall output
for row in rows:
    print(row)


# close database connection
con.close()
