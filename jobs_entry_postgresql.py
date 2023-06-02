# GUI tutorial here: https://realpython.com/python-gui-tkinter/
# psycopg2 documentation: https://pypi.org/project/psycopg2/
# https://www.psycopg.org/docs/install.html#install-from-source

import psycopg2
from tkinter import *


def main():

    # create window
    window = Tk()
    window.title("Jobs Applied To")
    window.geometry('400x400')

    # function to store values and insert them into the database
    def handle_CompanyName():
        name = enterCompany.get()
        position = enterPosition.get()
        date = enterDate.get()
        # insert event handlers
        # open connection to database

        con = psycopg2.connect(database="<db_name>",
                               host="localhost",
                               user="postgres",
                               password="<pwd>",
                               port="<port>")

        # create cursor
        cur = con.cursor()

        # create table if it does not exist
        cur.execute("create table IF NOT EXISTS jobs_applied(company varchar(80), title varchar(80), date varchar(80))")

        # Insert values saved into database (date as YYYY-MM-DD)
        query = """INSERT INTO jobs_applied (company, title, date) values (%s, %s, %s)"""
        data = (name, position, date)
        cur.execute(query, data)

        # commit
        con.commit()
        print("Commit complete")

        # execute query
        cur.execute("select * from jobs_applied")
        rows = cur.fetchall()

        # loop the cursor to view the fetchall output
        for row in rows:
            print(row)

        # close connection
        cur.close()
        con.close()
        print(f"On {date}, applied for {position} at {name}")

    # create widgets - 3 labels, 3 entry widgets, and button widget
    company_label = Label(text="Enter Company Name", width=30)
    company_label.pack()
    enterCompany = Entry(window, width=30)
    enterCompany.pack()

    position_label = Label(text="Enter Position Applied For")
    position_label.pack()
    enterPosition = Entry(window, width=30)
    enterPosition.pack()

    date_label = Label(text="Enter Date Applied on YYYY-MM-DD")
    date_label.pack()
    enterDate = Entry(width=30)
    enterDate.pack()

    Button(window,
           text="Insert Values into the Database",
           width=30,
           padx=5,
           pady=5,
           command=handle_CompanyName
           ).pack()

    window.mainloop()


if __name__ == '__main__':
    main()
