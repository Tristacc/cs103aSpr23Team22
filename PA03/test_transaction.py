
import sqlite3
import os
from transactions import Transaction

#---------------------------------test from Trista -----------------------------------
transaction = Transaction()
sample_item = {
    'item_num': 1,
    'amount': 50,
    'category': 'Groceries',
    'date': '0205',
    'description': 'Bread and milk'
}

# prepare -- clear table
def clearTable():
    con= sqlite3.connect(os.getenv('HOME')+'/Desktop/cs103aSpr23Team22/PA03/tracker.db')
    cur = con.cursor() 
    cur.execute("DELETE FROM transactions")
    con.commit()
    con.close()

# get number of data in the table
def num_data():
    con= sqlite3.connect(os.getenv('HOME')+'/Desktop/cs103aSpr23Team22/PA03/tracker.db')
    cur = con.cursor() 
    cur.execute("SELECT COUNT(*) FROM transactions")
    count = cur.fetchone()[0]
    con.close()
    return count

def test_add():
    initial_num = num_data()
    #add one data
    transaction.add(sample_item)
    count =  num_data()
    assert count == initial_num + 1

def test_delete():
    userInput = {'item_num':1}
    transaction.delete(userInput)
    count =  num_data()
    assert count == 0
#----------------------------end of test from Trista -----------------------------------
