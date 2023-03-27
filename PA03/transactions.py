'''It should be similar to the Todolist ORM from Lesson 19 in class. It will allow the user to read and update the database as need.
The transaction class should not do any printing!! '''
import sqlite3
import os

def toDict(t,str):
    if str == "": 
        transaction = {
        'rowid':t[0], 
        'item_num':t[1], 
        'amount':t[2], 
        'category':t[3],
        'date':t[4],
        'description':t[5]
        }
    elif str == "date":
        transaction = {
        'rowid':t[0], 
        'date':t[1], 
        'item_num':t[2], 
        'amount':t[3],
        'category':t[4],
        'description':t[5]
        }
    elif str == "category":
        transaction = {
        'rowid':t[0], 
        'amount':t[1],
        'category':t[2],
        }
    return transaction

class Transaction():
    #---------------------------------methods from Trista -----------------------------------
    def __init__(self):
        self.runQuery('''CREATE TABLE IF NOT EXISTS transactions
                    (item_num int, amount int, category text, date int, description text)''',(),"")
    def add(self, item):
        '''add the itemds to table'''
        return self.runQuery("INSERT INTO transactions VALUES(?,?,?,?,?)",(item['item_num'],item['amount'],item['category'],item['date'],item['description']),"")
    def show_transactions(self):
        '''show the table'''
        return self.runQuery("SELECT rowid,* from transactions",(),"")
    def delete(self, item):
        '''delete itemds by item_num'''
        return self.runQuery("DELETE FROM transactions WHERE item_num=(?)",(item['item_num'],),"")
    #-----------------------------end of methods from Trista -----------------------------------

    #---------------------------------methods from Kaiyu----------------------------------------
    def summarize_by_date(self):
        '''summarize items by date'''
        return self.runQuery("SELECT rowid, date, item_num, SUM(amount), category, description FROM transactions GROUP BY date, item_num ORDER BY date ASC",(),"date")
    def summarize_by_month(self):
        '''summarize items by month'''
        return self.runQuery("SELECT rowid, STRFTIME('%Y-%m', date) as month, item_num, SUM(amount), category, description FROM transactions GROUP BY month, item_num ORDER BY month ASC",(),"date")
    #-----------------------------end of methods from Kaiyu------------------------------------

    #---------------------------------methods from Chenchuhui----------------------------------------
    def summarize_by_year(self):
        print(self.runQuery("SELECT rowid, STRFTIME('%Y', date) as year, item_num, SUM(amount), category, description FROM transactions GROUP BY year, item_num ORDER BY year ASC",(),"date"))
        return self.runQuery("SELECT rowid, STRFTIME('%Y', date) as year, item_num, SUM(amount), category, description FROM transactions GROUP BY year, item_num ORDER BY year ASC",(),"date")

    def summarize_by_category(self):
        return self.runQuery("SELECT rowid, SUM(amount), category FROM transactions GROUP BY category ORDER BY category ASC",(),"category")


    #-----------------------------end of methods from Chenchuhui------------------------------------
    def runQuery(self,query,tuple,str):
        con= sqlite3.connect(os.getcwd()+'/tracker.db')
        cur = con.cursor() 
        cur.execute(query,tuple)
        tuples = cur.fetchall()
        con.commit()
        con.close()
        return [toDict(t,str) for t in tuples]
