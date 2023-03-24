'''It should be similar to the Todolist ORM from Lesson 19 in class. It will allow the user to read and update the database as need.
The transaction class should not do any printing!! '''
import sqlite3
import os

def toDict(t):
    transaction = {
        'rowid':t[0], 
        'item_num':t[1], 
        'amount':t[2], 
        'category':t[3],
        'date':t[4],
        'description':t[5]
    }
    return transaction
class Transaction():
    #---------------------------------methods from Trista -----------------------------------
    def __init__(self):
        self.runQuery('''CREATE TABLE IF NOT EXISTS transactions
                    (item_num int, amount int, category text, date int, description text)''',())
    def add(self, item):
        '''add the itemds to table'''
        return self.runQuery("INSERT INTO transactions VALUES(?,?,?,?,?)",(item['item_num'],item['amount'],item['category'],item['date'],item['description']))
    def show_transactions(self):
        '''show the table'''
        return self.runQuery("SELECT rowid,* from transactions",())
    def delete(self, item):
        '''delete itemds by item_num'''
        return self.runQuery("DELETE FROM transactions WHERE item_num=(?)",(item['item_num'],))
    #-----------------------------end of methods from Trista -----------------------------------
    def runQuery(self,query,tuple):
        con= sqlite3.connect(os.getenv('HOME')+'/Desktop/cs103aSpr23Team22/PA03/tracker.db')
        cur = con.cursor() 
        cur.execute(query,tuple)
        tuples = cur.fetchall()
        con.commit()
        con.close()
        return [toDict(t) for t in tuples]
